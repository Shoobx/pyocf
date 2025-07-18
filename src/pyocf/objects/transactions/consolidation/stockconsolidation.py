"""Object describing a consolidation of stock positions"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/main/schema/objects/transactions/consolidation/StockConsolidation.schema.jso
# n

from pydantic import Field
from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.consolidation.consolidation import (
    Consolidation,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from typing import Annotated
from typing import Literal
from typing import Optional


class StockConsolidation(Object, Transaction, Consolidation):
    """Object describing a consolidation of stock positions"""

    object_type: Annotated[Literal["TX_STOCK_CONSOLIDATION"], Field(description="")] = (
        "TX_STOCK_CONSOLIDATION"
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
    security_ids: Annotated[
        list[str],
        Field(
            description="Array of identifiers for the security (or securities) being consolidation as a"
            "result of the transaction"
        ),
    ]
    date: Annotated[Date, Field(description="Date on which the transaction occurred")]
    resulting_security_id: Annotated[
        str,
        Field(
            description="Identifier for the security that holds the consolidated balance from this"
            "transaction"
        ),
    ]
    reason_text: Optional[
        Annotated[
            str,
            Field(
                description="Free-form human-readable reason for stock consolidation"
            ),
        ]
    ] = None
