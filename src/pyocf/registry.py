"""OCF type map"""

OCF_TYPE_MAP = {
    "VALUATION": ("pyocf.objects.valuation", "Valuation"),
    "ISSUER": ("pyocf.objects.issuer", "Issuer"),
    "STAKEHOLDER": ("pyocf.objects.stakeholder", "Stakeholder"),
    "STOCK_LEGEND_TEMPLATE": (
        "pyocf.objects.stocklegendtemplate",
        "StockLegendTemplate",
    ),
    "STOCK_PLAN": ("pyocf.objects.stockplan", "StockPlan"),
    "VESTING_TERMS": ("pyocf.objects.vestingterms", "VestingTerms"),
    "STOCK_CLASS": ("pyocf.objects.stockclass", "StockClass"),
    "TX_STOCK_ACCEPTANCE": (
        "pyocf.objects.transactions.acceptance.stockacceptance",
        "StockAcceptance",
    ),
    "TX_PLAN_SECURITY_ACCEPTANCE": (
        "pyocf.objects.transactions.acceptance.plansecurityacceptance",
        "PlanSecurityAcceptance",
    ),
    "TX_WARRANT_ACCEPTANCE": (
        "pyocf.objects.transactions.acceptance.warrantacceptance",
        "WarrantAcceptance",
    ),
    "TX_CONVERTIBLE_ACCEPTANCE": (
        "pyocf.objects.transactions.acceptance.convertibleacceptance",
        "ConvertibleAcceptance",
    ),
    "TX_VESTING_ACCELERATION": (
        "pyocf.objects.transactions.vesting.vestingacceleration",
        "VestingAcceleration",
    ),
    "TX_VESTING_EVENT": (
        "pyocf.objects.transactions.vesting.vestingevent",
        "VestingEvent",
    ),
    "TX_VESTING_START": (
        "pyocf.objects.transactions.vesting.vestingstart",
        "VestingStart",
    ),
    "TX_CONVERTIBLE_CANCELLATION": (
        "pyocf.objects.transactions.cancellation.convertiblecancellation",
        "ConvertibleCancellation",
    ),
    "TX_WARRANT_CANCELLATION": (
        "pyocf.objects.transactions.cancellation.warrantcancellation",
        "WarrantCancellation",
    ),
    "TX_STOCK_CANCELLATION": (
        "pyocf.objects.transactions.cancellation.stockcancellation",
        "StockCancellation",
    ),
    "TX_PLAN_SECURITY_CANCELLATION": (
        "pyocf.objects.transactions.cancellation.plansecuritycancellation",
        "PlanSecurityCancellation",
    ),
    "TX_PLAN_SECURITY_RELEASE": (
        "pyocf.objects.transactions.release.plansecurityrelease",
        "PlanSecurityRelease",
    ),
    "TX_STOCK_CLASS_SPLIT": (
        "pyocf.objects.transactions.split.stockclasssplit",
        "StockClassSplit",
    ),
    "TX_PLAN_SECURITY_TRANSFER": (
        "pyocf.objects.transactions.transfer.plansecuritytransfer",
        "PlanSecurityTransfer",
    ),
    "TX_CONVERTIBLE_TRANSFER": (
        "pyocf.objects.transactions.transfer.convertibletransfer",
        "ConvertibleTransfer",
    ),
    "TX_STOCK_TRANSFER": (
        "pyocf.objects.transactions.transfer.stocktransfer",
        "StockTransfer",
    ),
    "TX_WARRANT_TRANSFER": (
        "pyocf.objects.transactions.transfer.warranttransfer",
        "WarrantTransfer",
    ),
    "TX_PLAN_SECURITY_EXERCISE": (
        "pyocf.objects.transactions.exercise.plansecurityexercise",
        "PlanSecurityExercise",
    ),
    "TX_WARRANT_EXERCISE": (
        "pyocf.objects.transactions.exercise.warrantexercise",
        "WarrantExercise",
    ),
    "TX_CONVERTIBLE_CONVERSION": (
        "pyocf.objects.transactions.conversion.convertibleconversion",
        "ConvertibleConversion",
    ),
    "TX_STOCK_CONVERSION": (
        "pyocf.objects.transactions.conversion.stockconversion",
        "StockConversion",
    ),
    "TX_STOCK_REPURCHASE": (
        "pyocf.objects.transactions.repurchase.stockrepurchase",
        "StockRepurchase",
    ),
    "TX_STOCK_CLASS_CONVERSION_RATIO_ADJUSTMENT": (
        "pyocf.objects.transactions.adjustment.stockclassconversionratioadjustment",
        "StockClassConversionRatioAdjustment",
    ),
    "TX_STOCK_PLAN_POOL_ADJUSTMENT": (
        "pyocf.objects.transactions.adjustment.stockplanpooladjustment",
        "StockPlanPoolAdjustment",
    ),
    "TX_STOCK_CLASS_AUTHORIZED_SHARES_ADJUSTMENT": (
        "pyocf.objects.transactions.adjustment.stockclassauthorizedsharesadjustment",
        "StockClassAuthorizedSharesAdjustment",
    ),
    "TX_CONVERTIBLE_RETRACTION": (
        "pyocf.objects.transactions.retraction.convertibleretraction",
        "ConvertibleRetraction",
    ),
    "TX_PLAN_SECURITY_RETRACTION": (
        "pyocf.objects.transactions.retraction.plansecurityretraction",
        "PlanSecurityRetraction",
    ),
    "TX_WARRANT_RETRACTION": (
        "pyocf.objects.transactions.retraction.warrantretraction",
        "WarrantRetraction",
    ),
    "TX_STOCK_RETRACTION": (
        "pyocf.objects.transactions.retraction.stockretraction",
        "StockRetraction",
    ),
    "TX_PLAN_SECURITY_ISSUANCE": (
        "pyocf.objects.transactions.issuance.plansecurityissuance",
        "PlanSecurityIssuance",
    ),
    "TX_WARRANT_ISSUANCE": (
        "pyocf.objects.transactions.issuance.warrantissuance",
        "WarrantIssuance",
    ),
    "TX_CONVERTIBLE_ISSUANCE": (
        "pyocf.objects.transactions.issuance.convertibleissuance",
        "ConvertibleIssuance",
    ),
    "TX_STOCK_ISSUANCE": (
        "pyocf.objects.transactions.issuance.stockissuance",
        "StockIssuance",
    ),
    "TX_STOCK_REISSUANCE": (
        "pyocf.objects.transactions.reissuance.stockreissuance",
        "StockReissuance",
    ),
    "RATIO_CONVERSION": (
        "pyocf.types.conversion_mechanisms.ratioconversionmechanism",
        "RatioConversionMechanism",
    ),
    "CONVERTIBLE_NOTE_CONVERSION": (
        "pyocf.types.conversion_mechanisms.noteconversionmechanism",
        "NoteConversionMechanism",
    ),
    "CUSTOM_CONVERSION": (
        "pyocf.types.conversion_mechanisms.customconversionmechanism",
        "CustomConversionMechanism",
    ),
    "SAFE_CONVERSION": (
        "pyocf.types.conversion_mechanisms.safeconversionmechanism",
        "SAFEConversionMechanism",
    ),
    "FIXED_PERCENT_OF_CAPITALIZATION_CONVERSION": (
        "pyocf.types.conversion_mechanisms.percentcapitalizationconversionmechanism",
        "PercentCapitalizationConversionMechanism",
    ),
    "FIXED_AMOUNT_CONVERSION": (
        "pyocf.types.conversion_mechanisms.fixedamountconversionmechanism",
        "FixedAmountConversionMechanism",
    ),
    "VESTING_SCHEDULE_RELATIVE": (
        "pyocf.types.vesting.vestingschedulerelativetrigger",
        "VestingScheduleRelativeTrigger",
    ),
    "MONTHS": ("pyocf.types.vesting.vestingperiodinmonths", "VestingPeriodInMonths"),
    "VESTING_SCHEDULE_ABSOLUTE": (
        "pyocf.types.vesting.vestingscheduleabsolutetrigger",
        "VestingScheduleAbsoluteTrigger",
    ),
    "DAYS": ("pyocf.types.vesting.vestingperiodindays", "VestingPeriodInDays"),
    "VESTING_EVENT": ("pyocf.types.vesting.vestingeventtrigger", "VestingEventTrigger"),
    "VESTING_START_DATE": (
        "pyocf.types.vesting.vestingstarttrigger",
        "VestingStartTrigger",
    ),
    "AUTOMATIC_ON_DATE": (
        "pyocf.types.conversion_triggers.automaticconversionondatetrigger",
        "AutomaticConversionOnDateTrigger",
    ),
    "ELECTIVE_ON_CONDITION": (
        "pyocf.types.conversion_triggers.electiveconversiononconditiontrigger",
        "ElectiveConversionOnConditionTrigger",
    ),
    "ELECTIVE_IN_RANGE": (
        "pyocf.types.conversion_triggers.electiveconversionindaterangetrigger",
        "ElectiveConversionInDateRangeTrigger",
    ),
    "ELECTIVE_AT_WILL": (
        "pyocf.types.conversion_triggers.electiveconversionatwilltrigger",
        "ElectiveConversionAtWillTrigger",
    ),
    "UNSPECIFIED": (
        "pyocf.types.conversion_triggers.unspecifiedconversiontrigger",
        "UnspecifiedConversionTrigger",
    ),
    "AUTOMATIC_ON_CONDITION": (
        "pyocf.types.conversion_triggers.automaticconversiononconditiontrigger",
        "AutomaticConversionOnConditionTrigger",
    ),
    "CONVERTIBLE_CONVERSION_RIGHT": (
        "pyocf.types.conversion_rights.convertibleconversionright",
        "ConvertibleConversionRight",
    ),
    "WARRANT_CONVERSION_RIGHT": (
        "pyocf.types.conversion_rights.warrantconversionright",
        "WarrantConversionRight",
    ),
    "STOCK_CLASS_CONVERSION_RIGHT": (
        "pyocf.types.conversion_rights.stockclassconversionright",
        "StockClassConversionRight",
    ),
    "OCF_STOCK_CLASSES_FILE": ("pyocf.files.stockclassesfile", "StockClassesFile"),
    "OCF_VESTING_TERMS_FILE": ("pyocf.files.vestingtermsfile", "VestingTermsFile"),
    "OCF_STOCK_LEGEND_TEMPLATES_FILE": (
        "pyocf.files.stocklegendtemplatesfile",
        "StockLegendTemplatesFile",
    ),
    "OCF_STAKEHOLDERS_FILE": ("pyocf.files.stakeholdersfile", "StakeholdersFile"),
    "OCF_MANIFEST_FILE": ("pyocf.files.ocfmanifestfile", "OCFManifestFile"),
    "OCF_STOCK_PLANS_FILE": ("pyocf.files.stockplansfile", "StockPlansFile"),
    "OCF_VALUATIONS_FILE": ("pyocf.files.valuationsfile", "ValuationsFile"),
    "OCF_TRANSACTIONS_FILE": ("pyocf.files.transactionsfile", "TransactionsFile"),
}
