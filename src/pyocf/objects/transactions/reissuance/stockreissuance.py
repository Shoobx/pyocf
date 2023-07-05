"""Object describing a re-issuance of stock"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/objects/transactions/reissuance/StockReissuance.schema.json

from pydantic import Field
from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.reissuance.reissuance import Reissuance
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from typing import Annotated
from typing import Literal
from typing import Optional


class StockReissuance(Object, Transaction, SecurityTransaction, Reissuance):
    """Object describing a re-issuance of stock"""

    object_type: Annotated[
        Literal["TX_STOCK_REISSUANCE"], Field(description="")
    ] = "TX_STOCK_REISSUANCE"
    id: Annotated[str, Field(description="Identifier for the object")]
    comments: Optional[
        Annotated[
            list[str],
            Field(
                description="Unstructured text comments related to and stored for the object"
            ),
        ]
    ]
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
    resulting_security_ids: Annotated[
        list[str],
        Field(
            description="Identifier of the new security (or securities) issuance resulting from a"
            "reissuance"
        ),
    ]
    split_transaction_id: Optional[
        Annotated[
            str,
            Field(
                description="When stock is reissued as a result of a stock split, this field contains id of"
                "the respective stock class split transaction. It is not set otherwise."
            ),
        ]
    ]
    reason_text: Optional[
        Annotated[
            str,
            Field(description="Free-form human-readable reason for stock reissuance"),
        ]
    ]
