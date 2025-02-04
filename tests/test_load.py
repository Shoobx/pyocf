# Copyright © 2023 FMR LLC

import datetime
import decimal
import json

from pathlib import Path
from pyocf import api
from pyocf.captable import Captable

sample_path = Path(Path(__file__).parent.parent, "Open-Cap-Format-OCF/samples")


def test_load_sample_manifest():
    path = Path(Path(__file__).parent, Path(sample_path, "Manifest.ocf.json"))
    with path.open("rt") as infile:
        obj = api.OCFManifestFile(**json.load(infile))

    assert obj.comments == [
        "This is an optional comment",
        """These md5 hashes are just dummy values. They've not been recalculated """
        """in a long time, but we should look into recalculating them dynamically """
        """via an actions or pre-commit hook.""",
    ]
    assert len(obj.stakeholders_files) == 1
    assert isinstance(obj.stakeholders_files[0], api.File)


def test_load_sample_stakeholders():
    path = Path(Path(__file__).parent, Path(sample_path, "Stakeholders.ocf.json"))
    with path.open("rt") as infile:
        obj = api.StakeholdersFile(**json.load(infile))
    assert len(obj.items) == 4
    item = obj.items[0]
    assert isinstance(item, api.Stakeholder)
    assert item.object_type == "STAKEHOLDER"
    assert isinstance(item.name, api.Name)


def test_load_sample_stock_classes():
    path = Path(Path(__file__).parent, Path(sample_path, "StockClasses.ocf.json"))
    with path.open("rt") as infile:
        obj = api.StockClassesFile(**json.load(infile))

    assert len(obj.items) == 2
    item = obj.items[0]
    assert isinstance(item, api.StockClass)
    assert item.object_type == "STOCK_CLASS"
    assert item.name == "Common Stock"
    assert item.class_type == api.StockClassType.ENUM_COMMON
    assert isinstance(item.par_value, api.Monetary)
    assert item.par_value.currency == "USD"
    assert item.par_value.amount == decimal.Decimal("0.0001000000")

    item = obj.items[1]
    assert item.class_type == api.StockClassType.ENUM_PREFERRED


def test_load_sample_stock_legend_templates():
    path = Path(Path(__file__).parent, Path(sample_path, "StockLegends.ocf.json"))
    with path.open("rt") as infile:
        obj = api.StockLegendTemplatesFile(**json.load(infile))

    assert len(obj.items) == 1
    item = obj.items[0]
    assert isinstance(item, api.StockLegendTemplate)
    item.object_type == "STOCK_LEGEND_TEMPLATE"
    item.name == "1933 Act Legend"


def test_load_sample_stock_plans():
    path = Path(Path(__file__).parent, Path(sample_path, "StockPlans.ocf.json"))
    with path.open("rt") as infile:
        obj = api.StockPlansFile(**json.load(infile))
    assert len(obj.items) == 1
    item = obj.items[0]
    assert isinstance(item, api.StockPlan)
    assert item.object_type == "STOCK_PLAN"
    assert item.plan_name == "2021 Stock Incentive Plan"
    assert item.board_approval_date == datetime.date(1983, 12, 31)
    assert item.initial_shares_reserved == decimal.Decimal("10000000")
    assert item.stock_class_ids == ["8d8371e8-d41d-4a49-9f42-b91758fd155d"]
    assert item.comments == [
        "Using new form of SOP released by Firm Y's benefits & comp team on 10/10/2021."
    ]


def test_load_sample_transactions():
    path = Path(Path(__file__).parent, Path(sample_path, "Transactions.ocf.json"))
    with path.open("rt") as infile:
        obj = api.TransactionsFile(**json.load(infile))
    item = obj.items[2]
    assert isinstance(item, api.ConvertibleAcceptance)
    assert item.id == "test-convertible-acceptance-minimal"
    assert item.security_id == "2936wa8yefhdsvcn"
    assert item.object_type == "TX_CONVERTIBLE_ACCEPTANCE"
    assert item.date == datetime.date(2022, 1, 20)

    item = obj.items[10]
    assert isinstance(item, api.ConvertibleIssuance)
    assert item.id == "test-convertible-issuance-minimal"
    assert item.security_id == "con_123456"
    assert item.object_type == "TX_CONVERTIBLE_ISSUANCE"
    assert item.date == datetime.date(1978, 5, 27)
    assert item.comments is None
    trigger = item.conversion_triggers[0]
    assert isinstance(
        trigger,
        api.AutomaticConversionOnDateTrigger,
    )
    assert trigger.type == "AUTOMATIC_ON_DATE"
    assert trigger.trigger_id == "CN-1.TRIG.1"
    assert trigger.nickname == "Converts on Maturity"
    assert (
        trigger.trigger_description == "The note shall convert on the date of maturity"
    )
    assert trigger.trigger_date == datetime.date(2022, 1, 1)

    cr = trigger.conversion_right
    assert isinstance(cr, api.ConvertibleConversionRight)
    assert cr.type == "CONVERTIBLE_CONVERSION_RIGHT"
    cm = cr.conversion_mechanism
    assert isinstance(cm, api.NoteConversionMechanism)
    assert cm.type == "CONVERTIBLE_NOTE_CONVERSION"
    assert cm.day_count_convention == api.DayCountType.ENUM_ACTUAL_365
    assert cm.interest_payout == api.InterestPayoutType.ENUM_DEFERRED
    assert cm.interest_accrual_period == api.AccrualPeriodType.ENUM_MONTHLY
    assert cm.compounding_type == api.CompoundingType.ENUM_COMPOUNDING
    assert cm.conversion_discount is None
    assert cm.conversion_valuation_cap is None
    assert cm.exit_multiple is None
    assert cm.conversion_mfn is None
    ir = cm.interest_rates[0]
    assert isinstance(ir, api.InterestRate)
    assert ir.rate == "0.0899"
    assert ir.accrual_start_date == datetime.date(2021, 1, 1)
    assert ir.accrual_end_date is None

    item = obj.items[64]
    assert isinstance(item, api.WarrantAcceptance)
    assert item.id == "test-warrant-acceptance-full-fields"
    assert item.security_id == "test-security-id"
    assert item.object_type == "TX_WARRANT_ACCEPTANCE"
    assert item.date == datetime.date(2022, 2, 1)
    assert item.comments == ["Here is a comment", "Here is another comment"]

    item = obj.items[69]
    assert isinstance(item, api.WarrantIssuance)
    assert item.id == "test-warrant-issuance-minimal"
    assert item.custom_id == "W-1"
    assert item.object_type == "TX_WARRANT_ISSUANCE"
    assert isinstance(item.exercise_price, api.Monetary)
    assert item.exercise_price.amount == 1
    assert isinstance(item.purchase_price, api.Monetary)
    assert item.purchase_price.amount == 1

    et = item.exercise_triggers[0]
    assert isinstance(et, api.AutomaticConversionOnConditionTrigger)
    assert et.type == "AUTOMATIC_ON_CONDITION"
    assert et.trigger_id == "WARRANT-1.TRIG.1"
    assert et.nickname.startswith("Automatic exercise immediately prior to")

    cr = et.conversion_right
    assert isinstance(cr, api.WarrantConversionRight)
    assert cr.type == "WARRANT_CONVERSION_RIGHT"
    assert cr.converts_to_future_round is None
    assert cr.converts_to_stock_class_id == "stock-class-id"

    cm = cr.conversion_mechanism
    assert isinstance(cm, api.FixedAmountConversionMechanism)
    assert cm.type == "FIXED_AMOUNT_CONVERSION"
    assert cm.converts_to_quantity == decimal.Decimal("10000.00")

    item = obj.items[76]
    assert isinstance(item, api.WarrantRetraction)
    assert item.id == "test-warrant-retraction-full-fields"
    assert item.security_id == "test-security-id"
    assert item.object_type == "TX_WARRANT_RETRACTION"
    assert item.reason_text == "Need to retract"
    assert item.date == datetime.date(2022, 2, 1)
    assert item.comments == ["Here is a comment", "Here is another comment"]


def test_load_sample_valuations_files():
    path = Path(Path(__file__).parent, Path(sample_path, "Valuations.ocf.json"))
    with path.open("rt") as infile:
        obj = api.ValuationsFile(**json.load(infile))

    assert len(obj.items) == 1
    item = obj.items[0]
    assert isinstance(item, api.Valuation)
    item.object_type == "VALUATION"
    item.valuation_type == "409A",


def test_load_sample_vesting_terms():
    path = Path(Path(__file__).parent, Path(sample_path, "VestingTerms.ocf.json"))
    with path.open("rt") as infile:
        obj = api.VestingTermsFile(**json.load(infile))

    assert len(obj.items) == 5
    item = obj.items[0]
    assert isinstance(item, api.VestingTerms)
    item.object_type == "VESTING_TERMS"
    assert item.name == "Four Year / One Year Cliff"
    assert item.allocation_type == api.AllocationType.ENUM_CUMULATIVE_ROUNDING

    assert len(item.vesting_conditions) == 3
    assert isinstance(item.vesting_conditions[0], api.VestingCondition)
    assert item.vesting_conditions[0].id == "vesting-start"
    assert item.vesting_conditions[0].next_condition_ids == ["cliff"]

    # Vesting conditions can have different trigger types
    condition = item.vesting_conditions[0]
    assert isinstance(condition.trigger, api.VestingStartTrigger)
    assert condition.portion is None

    condition = item.vesting_conditions[1]
    assert isinstance(condition.portion, api.VestingConditionPortion)
    # You can instantiate simple types by just passing in the value
    assert condition.portion.numerator == api.Numeric("12")
    # But pydantic will pass it in with the name "__root__"
    assert condition.portion.denominator == api.Numeric(root="48")

    trigger = condition.trigger
    assert isinstance(trigger, api.VestingScheduleRelativeTrigger)
    assert isinstance(trigger.period, api.VestingPeriodInMonths)
    assert trigger.period.length == 12
    assert trigger.period.occurrences == 1
    assert (
        trigger.period.day_of_month
        == api.VestingDayOfMonth.ENUM_VESTING_START_DAY_OR_LAST_DAY_OF_MONTH
    )

    condition = item.vesting_conditions[2]
    trigger = condition.trigger
    assert trigger.period.length == 1
    assert trigger.period.occurrences == 36

    item = obj.items[1]
    assert item.allocation_type == api.AllocationType.ENUM_CUMULATIVE_ROUND_DOWN
    assert len(item.vesting_conditions) == 8
    assert isinstance(item.vesting_conditions[0], api.VestingCondition)
    assert item.vesting_conditions[0].id == "vesting-start"

    condition = item.vesting_conditions[1]
    assert condition.portion is None
    assert condition.quantity == 0

    condition = item.vesting_conditions[2]
    assert condition.portion.numerator == 1
    assert condition.portion.denominator == 1

    trigger = condition.trigger
    assert isinstance(trigger, api.VestingEventTrigger)
    assert trigger.type == "VESTING_EVENT"

    item = obj.items[3]
    assert item.allocation_type == api.AllocationType.ENUM_BACK_LOADED

    item = obj.items[4]
    condition = item.vesting_conditions[4]
    assert condition.quantity == 0
    assert isinstance(
        condition.trigger,
        api.VestingScheduleAbsoluteTrigger,
    )
    assert condition.trigger.date == datetime.date(2017, 4, 1)


def test_load_captable_directory():
    path = Path(Path(__file__).parent, Path(sample_path, "Manifest.ocf.json"))
    # Just check that each type of data is not empty, ie, that it has been loaded.
    # The above tests check that the loading works corrcetly.
    captable = Captable.load(path)
    assert captable.manifest
    assert captable.stakeholders
    assert captable.stock_classes
    assert captable.stock_legend_templates
    assert captable.stock_plans
    assert captable.transactions
    assert captable.valuations
    assert captable.vesting_terms


def test_load_captable_zipfile():
    path = Path(Path(__file__).parent, "samples/Captable.ocf.zip")
    # Just check that each type of data is not empty, ie, that it has been loaded.
    # The above tests check that the loading works corrcetly.
    captable = Captable.load(path)
    assert captable.manifest
    assert captable.stakeholders
    assert captable.stock_classes
    assert captable.stock_legend_templates
    assert captable.stock_plans
    assert captable.transactions
    assert captable.valuations
    assert captable.vesting_terms


def test_load_captable_filelike():
    path = Path(Path(__file__).parent, "samples/Captable.ocf.zip")
    # Just check that each type of data is not empty, ie, that it has been loaded.
    # The above tests check that the loading works corrcetly.
    with open(path, "rb") as file:
        captable = Captable.load(file)
    assert captable.manifest
    assert captable.stakeholders
    assert captable.stock_classes
    assert captable.stock_legend_templates
    assert captable.stock_plans
    assert captable.transactions
    assert captable.valuations
    assert captable.vesting_terms
