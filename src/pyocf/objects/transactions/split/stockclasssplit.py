"""Object describing a split of a stock class"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/objects/transactions/split/StockClassSplit.schema.json

from pydantic import Field
from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.stockclasstransaction import (
    StockClassTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from pyocf.types.ratio import Ratio
from typing import Annotated
from typing import Literal
from typing import Optional


class StockClassSplit(Object, Transaction, StockClassTransaction):
    """Object describing a split of a stock class"""

    object_type: Annotated[Literal["TX_STOCK_CLASS_SPLIT"], Field(description="")] = (
        "TX_STOCK_CLASS_SPLIT"
    )
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
    split_ratio: Annotated[
        Ratio,
        Field(
            description="Ratio of new shares to old shares. For 2-for-1 split the numerator of the ratio"
            "is 2 and the denominator is 1."
        ),
    ]
