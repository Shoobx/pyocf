"""Object describing a stock issuance transaction by the issuer and held by a
stakeholder"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/objects/transactions/issuance/StockIssuance.schema.json

from pydantic import Field
from pyocf.enums.stockissuancetype import StockIssuanceType
from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.issuance.issuance import Issuance
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from pyocf.types.monetary import Monetary
from pyocf.types.numeric import Numeric
from pyocf.types.securityexemption import SecurityExemption
from pyocf.types.sharenumberrange import ShareNumberRange
from pyocf.types.vesting import Vesting
from typing import Annotated
from typing import Literal
from typing import Optional


class StockIssuance(Object, Transaction, SecurityTransaction, Issuance):
    """Object describing a stock issuance transaction by the issuer and held by a
    stakeholder
    """

    object_type: Annotated[Literal["TX_STOCK_ISSUANCE"], Field(description="")] = (
        "TX_STOCK_ISSUANCE"
    )
    stock_class_id: Annotated[
        str, Field(description="Identifier of the stock class for this stock issuance")
    ]
    stock_plan_id: Optional[
        Annotated[
            str,
            Field(
                description="Identifier of StockPlan the Stock was issued from (in the case of RSAs or Stock"
                "issued from a plan)."
            ),
        ]
    ] = None
    share_numbers_issued: Optional[
        Annotated[
            list[ShareNumberRange],
            Field(
                description="Range(s) of the specific share numbers included in this issuance. This is"
                "different from a certificate number you might include in the `custom_id` field"
                "or the `security_id` created in this issuance. This field should be used where,"
                "for whatever reason, shares are not fungible and you must track, with each"
                "issuance, *which* specific share numbers are included in the issuance - e.g."
                "share numbers 1 - 100 and 250-300."
            ),
        ]
    ] = None
    share_price: Annotated[
        Monetary,
        Field(description="The price per share paid for the stock by the holder"),
    ]
    quantity: Annotated[
        Numeric, Field(description="Number of shares issued to the stakeholder")
    ]
    vesting_terms_id: Optional[
        Annotated[
            str,
            Field(
                description="Identifier of the VestingTerms to which this security is subject. If neither"
                "`vesting_terms_id` or `vestings` are present then the security is fully vested"
                "on issuance."
            ),
        ]
    ] = None
    vestings: Optional[
        Annotated[
            list[Vesting],
            Field(
                description="List of exact vesting dates and amounts for this security. When `vestings` array"
                "is present then `vesting_terms_id` may be ignored."
            ),
        ]
    ] = None
    cost_basis: Optional[
        Annotated[
            Monetary, Field(description="The cost basis for this particular stock")
        ]
    ] = None
    stock_legend_ids: Annotated[
        list[str],
        Field(description="List of stock legend ids that apply to this stock"),
    ]
    issuance_type: Optional[
        Annotated[
            StockIssuanceType,
            Field(
                description="Optional field to flag certain special types of issuances (like RSAs)"
            ),
        ]
    ] = None
    id: Annotated[str, Field(description="Identifier for the object")]
    comments: Optional[
        Annotated[
            list[str],
            Field(
                description="Unstructured text comments related to and stored for the object"
            ),
        ]
    ] = None
    security_id: Annotated[
        str,
        Field(
            description="Identifier for the security (stock, plan security, warrant, or convertible) by"
            "which it can be referenced by other transaction objects. Note that while this"
            "identifier is created with an issuance object, it should be different than the"
            "issuance object's `id` field which identifies the issuance transaction object"
            "itself. All future transactions on the security (e.g. acceptance, transfer,"
            "cancel, etc.) must reference this `security_id` to qualify which security the"
            "transaction applies to."
        ),
    ]
    date: Annotated[Date, Field(description="Date on which the transaction occurred")]
    custom_id: Annotated[
        str, Field(description="A custom ID for this security (e.g. CN-1.)")
    ]
    stakeholder_id: Annotated[
        str,
        Field(
            description="Identifier for the stakeholder that holds legal title to this security"
        ),
    ]
    board_approval_date: Optional[
        Annotated[Date, Field(description="Date of board approval for the security")]
    ] = None
    stockholder_approval_date: Optional[
        Annotated[
            Date,
            Field(description="Date on which the stockholders approved the security"),
        ]
    ] = None
    consideration_text: Optional[
        Annotated[
            str,
            Field(
                description="Unstructured text description of consideration provided in exchange for security"
                "issuance"
            ),
        ]
    ] = None
    security_law_exemptions: Annotated[
        list[SecurityExemption],
        Field(
            description="List of security law exemptions (and applicable jurisdictions) for this security"
        ),
    ]
