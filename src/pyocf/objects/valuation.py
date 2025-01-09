"""Object describing a valuation used in the cap table"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.1.0/schema/objects/Valuation.schema.json

from pydantic import Field
from pyocf.enums.valuationtype import ValuationType
from pyocf.primitives.objects.object import Object
from pyocf.types.date import Date
from pyocf.types.monetary import Monetary
from typing import Annotated
from typing import Literal
from typing import Optional


class Valuation(Object):
    """Object describing a valuation used in the cap table"""

    object_type: Annotated[Literal["VALUATION"], Field(description="")] = "VALUATION"
    provider: Optional[
        Annotated[str, Field(description="Entity which provided the valuation")]
    ] = None
    board_approval_date: Optional[
        Annotated[
            Date,
            Field(
                description="Date on which board approved the valuation. This is essential for 409A"
                "valuations, in particular, which require the Board to approve the valuation."
            ),
        ]
    ] = None
    price_per_share: Annotated[Monetary, Field(description="Valued price per share")]
    effective_date: Annotated[
        Date, Field(description="Date on which this valuation is first valid")
    ]
    stock_class_id: Annotated[
        str, Field(description="Identifier of the stock class for this valuation")
    ]
    valuation_type: Annotated[
        ValuationType,
        Field(
            description="Seam for supporting different types of valuations in future versions"
        ),
    ]
    id: Annotated[str, Field(description="Identifier for the object")]
    comments: Optional[
        Annotated[
            list[str],
            Field(
                description="Unstructured text comments related to and stored for the object"
            ),
        ]
    ] = None
