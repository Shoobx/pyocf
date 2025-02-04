"""JSON containing file type identifier and list transactions"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/files/TransactionsFile.schema.json

from pydantic import Field
from pyocf.objects.transactions.acceptance.convertibleacceptance import (
    ConvertibleAcceptance,
)
from pyocf.objects.transactions.acceptance.equitycompensationacceptance import (
    EquityCompensationAcceptance,
)
from pyocf.objects.transactions.acceptance.plansecurityacceptance import (
    PlanSecurityAcceptance,
)
from pyocf.objects.transactions.acceptance.stockacceptance import StockAcceptance
from pyocf.objects.transactions.acceptance.warrantacceptance import WarrantAcceptance
from pyocf.objects.transactions.adjustment.issuerauthorizedsharesadjustment import (
    IssuerAuthorizedSharesAdjustment,
)
from pyocf.objects.transactions.adjustment.stockclassauthorizedsharesadjustment import (
    StockClassAuthorizedSharesAdjustment,
)
from pyocf.objects.transactions.adjustment.stockclassconversionratioadjustment import (
    StockClassConversionRatioAdjustment,
)
from pyocf.objects.transactions.adjustment.stockplanpooladjustment import (
    StockPlanPoolAdjustment,
)
from pyocf.objects.transactions.cancellation.convertiblecancellation import (
    ConvertibleCancellation,
)
from pyocf.objects.transactions.cancellation.equitycompensationcancellation import (
    EquityCompensationCancellation,
)
from pyocf.objects.transactions.cancellation.plansecuritycancellation import (
    PlanSecurityCancellation,
)
from pyocf.objects.transactions.cancellation.stockcancellation import StockCancellation
from pyocf.objects.transactions.cancellation.warrantcancellation import (
    WarrantCancellation,
)
from pyocf.objects.transactions.conversion.convertibleconversion import (
    ConvertibleConversion,
)
from pyocf.objects.transactions.conversion.stockconversion import StockConversion
from pyocf.objects.transactions.exercise.equitycompensationexercise import (
    EquityCompensationExercise,
)
from pyocf.objects.transactions.exercise.plansecurityexercise import (
    PlanSecurityExercise,
)
from pyocf.objects.transactions.exercise.warrantexercise import WarrantExercise
from pyocf.objects.transactions.issuance.convertibleissuance import ConvertibleIssuance
from pyocf.objects.transactions.issuance.equitycompensationissuance import (
    EquityCompensationIssuance,
)
from pyocf.objects.transactions.issuance.plansecurityissuance import (
    PlanSecurityIssuance,
)
from pyocf.objects.transactions.issuance.stockissuance import StockIssuance
from pyocf.objects.transactions.issuance.warrantissuance import WarrantIssuance
from pyocf.objects.transactions.reissuance.stockreissuance import StockReissuance
from pyocf.objects.transactions.release.equitycompensationrelease import (
    EquityCompensationRelease,
)
from pyocf.objects.transactions.release.plansecurityrelease import PlanSecurityRelease
from pyocf.objects.transactions.repurchase.stockrepurchase import StockRepurchase
from pyocf.objects.transactions.retraction.convertibleretraction import (
    ConvertibleRetraction,
)
from pyocf.objects.transactions.retraction.equitycompensationretraction import (
    EquityCompensationRetraction,
)
from pyocf.objects.transactions.retraction.plansecurityretraction import (
    PlanSecurityRetraction,
)
from pyocf.objects.transactions.retraction.stockretraction import StockRetraction
from pyocf.objects.transactions.retraction.warrantretraction import WarrantRetraction
from pyocf.objects.transactions.return_to_pool.stockplanreturntopool import (
    StockPlanReturnToPool,
)
from pyocf.objects.transactions.split.stockclasssplit import StockClassSplit
from pyocf.objects.transactions.transfer.convertibletransfer import ConvertibleTransfer
from pyocf.objects.transactions.transfer.equitycompensationtransfer import (
    EquityCompensationTransfer,
)
from pyocf.objects.transactions.transfer.plansecuritytransfer import (
    PlanSecurityTransfer,
)
from pyocf.objects.transactions.transfer.stocktransfer import StockTransfer
from pyocf.objects.transactions.transfer.warranttransfer import WarrantTransfer
from pyocf.objects.transactions.vesting.vestingacceleration import VestingAcceleration
from pyocf.objects.transactions.vesting.vestingevent import VestingEvent
from pyocf.objects.transactions.vesting.vestingstart import VestingStart
from pyocf.primitives.files.file import FileObject
from typing import Annotated
from typing import Literal
from typing import Union


class TransactionsFile(FileObject):
    """JSON containing file type identifier and list transactions"""

    items: Annotated[
        list[
            Annotated[
                Union[
                    ConvertibleAcceptance,
                    EquityCompensationAcceptance,
                    PlanSecurityAcceptance,
                    StockAcceptance,
                    WarrantAcceptance,
                    ConvertibleCancellation,
                    EquityCompensationCancellation,
                    PlanSecurityCancellation,
                    StockCancellation,
                    WarrantCancellation,
                    ConvertibleConversion,
                    StockConversion,
                    EquityCompensationExercise,
                    PlanSecurityExercise,
                    WarrantExercise,
                    ConvertibleIssuance,
                    EquityCompensationIssuance,
                    PlanSecurityIssuance,
                    StockIssuance,
                    WarrantIssuance,
                    StockReissuance,
                    StockRepurchase,
                    EquityCompensationRelease,
                    PlanSecurityRelease,
                    ConvertibleRetraction,
                    EquityCompensationRetraction,
                    PlanSecurityRetraction,
                    StockRetraction,
                    WarrantRetraction,
                    StockPlanReturnToPool,
                    StockClassSplit,
                    StockClassConversionRatioAdjustment,
                    StockClassAuthorizedSharesAdjustment,
                    ConvertibleTransfer,
                    EquityCompensationTransfer,
                    PlanSecurityTransfer,
                    StockTransfer,
                    WarrantTransfer,
                    VestingAcceleration,
                    VestingStart,
                    VestingEvent,
                    StockPlanPoolAdjustment,
                    IssuerAuthorizedSharesAdjustment,
                ],
                Field(discriminator="object_type"),
            ]
        ],
        Field(description="List of OCF transaction objects"),
    ]
    file_type: Annotated[Literal["OCF_TRANSACTIONS_FILE"], Field(description="")] = (
        "OCF_TRANSACTIONS_FILE"
    )
