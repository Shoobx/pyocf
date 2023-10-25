"""Object describing a stock repurchase transaction"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/objects/transactions/repurchase/StockRepurchase.schema.json

from pydantic import Field
from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.repurchase.repurchase import Repurchase
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from pyocf.types.monetary import Monetary
from pyocf.types.numeric import Numeric
from typing import Annotated
from typing import Literal
from typing import Optional


class StockRepurchase(Object, Transaction, SecurityTransaction, Repurchase):
    """Object describing a stock repurchase transaction"""

    object_type: Annotated[
        Literal["TX_STOCK_REPURCHASE"], Field(description="")
    ] = "TX_STOCK_REPURCHASE"
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
    price: Annotated[
        Monetary, Field(description="Repurchase price per share of the stock")
    ]
    quantity: Annotated[
        Numeric, Field(description="Number of shares of stock repurchased")
    ]
    consideration_text: Optional[
        Annotated[
            str,
            Field(
                description="Unstructured text description of consideration provided in exchange for security"
                "repurchase"
            ),
        ]
    ] = None
    balance_security_id: Optional[
        Annotated[
            str,
            Field(
                description="Identifier for the security that holds the remainder balance (for partial"
                "repurchases)"
            ),
        ]
    ] = None
