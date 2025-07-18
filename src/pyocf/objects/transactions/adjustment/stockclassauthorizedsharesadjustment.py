"""Object describing an event to change the number of authorized shares of a stock
class."""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.2.0/schema/objects/transactions/adjustment/StockClassAuthorizedSharesAdju
# stment.schema.json

from pydantic import Field
from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.stockclasstransaction import (
    StockClassTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from pyocf.types.numeric import Numeric
from typing import Annotated
from typing import Literal
from typing import Optional


class StockClassAuthorizedSharesAdjustment(Object, Transaction, StockClassTransaction):
    """Object describing an event to change the number of authorized shares of a stock
    class.
    """

    object_type: Annotated[
        Literal["TX_STOCK_CLASS_AUTHORIZED_SHARES_ADJUSTMENT"], Field(description="")
    ] = "TX_STOCK_CLASS_AUTHORIZED_SHARES_ADJUSTMENT"
    id: Annotated[str, Field(description="Identifier for the object")]
    comments: Optional[
        Annotated[
            list[str],
            Field(
                description="Unstructured text comments related to and stored for the object"
            ),
        ]
    ] = None
    date: Annotated[Date, Field(description="Date on which the transaction occurred")]
    stock_class_id: Annotated[
        str,
        Field(
            description="Identifier of the StockClass object, a subject of this transaction"
        ),
    ]
    new_shares_authorized: Annotated[
        Numeric,
        Field(
            description="The new number of shares authorized for this stock class as of the event of this"
            "transaction"
        ),
    ]
    board_approval_date: Optional[
        Annotated[
            Date,
            Field(
                description="Date on which the board approved the change to the stock class"
            ),
        ]
    ] = None
    stockholder_approval_date: Optional[
        Annotated[
            Date,
            Field(
                description="This optional field tracks when the stockholders approved the change to the"
                "stock class."
            ),
        ]
    ] = None
