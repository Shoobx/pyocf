"""Object describing a class of stock issued by the issuer"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/objects/StockClass.schema.json

from pydantic import Field
from pyocf.enums.authorizedshares import AuthorizedShares
from pyocf.enums.stockclasstype import StockClassType
from pyocf.primitives.objects.object import Object
from pyocf.types.conversion_rights.stockclassconversionright import (
    StockClassConversionRight,
)
from pyocf.types.date import Date
from pyocf.types.monetary import Monetary
from pyocf.types.numeric import Numeric
from typing import Annotated
from typing import Literal
from typing import Optional
from typing import Union


class StockClass(Object):
    """Object describing a class of stock issued by the issuer"""

    object_type: Annotated[Literal["STOCK_CLASS"], Field(description="")] = (
        "STOCK_CLASS"
    )
    name: Annotated[
        str,
        Field(
            description="Name for the stock type (e.g. Series A Preferred or Class A Common)"
        ),
    ]
    class_type: Annotated[
        StockClassType,
        Field(description="The type of this stock class (e.g. Preferred or Common)"),
    ]
    default_id_prefix: Annotated[
        str,
        Field(
            description="Default prefix for certificate numbers in certificated shares (e.g. CS- in"
            "CS-1). If certificate IDs have a dash, the prefix should end in the dash like"
            "CS-"
        ),
    ]
    initial_shares_authorized: Union[AuthorizedShares, Numeric]
    board_approval_date: Optional[
        Annotated[
            Date, Field(description="Date on which the board approved the stock class")
        ]
    ] = None
    stockholder_approval_date: Optional[
        Annotated[
            Date,
            Field(
                description="Date on which the stockholders approved the stock class"
            ),
        ]
    ] = None
    votes_per_share: Annotated[
        Numeric,
        Field(description="The number of votes each share of this stock class gets"),
    ]
    par_value: Optional[
        Annotated[
            Monetary, Field(description="Per-share par value of this stock class")
        ]
    ] = None
    price_per_share: Optional[
        Annotated[
            Monetary,
            Field(description="Per-share price this stock class was issued for"),
        ]
    ] = None
    seniority: Annotated[
        Numeric,
        Field(
            description="Seniority of the stock - determines repayment priority. Seniority is ordered by"
            "increasing number so that stock classes with a higher seniority have higher"
            "repayment priority. The following properties hold for all stock classes for a"
            "given company:"
            "a) transitivity: stock classes are absolutely stackable by seniority and in"
            "increasing numerical order,"
            "b) non-uniqueness: multiple stock classes can have the same Seniority number and"
            "therefore have the same liquidation/repayment order."
            "In practice, stock classes with same seniority may be created at different"
            "points in time and (for example, an extension of an existing preferred financing"
            "round), and also a new stock class can be created with seniority between two"
            "existing stock classes, in which case it is assigned some decimal number between"
            "the numbers representing seniority of the respective classes."
        ),
    ]
    conversion_rights: Optional[
        Annotated[
            list[StockClassConversionRight],
            Field(
                description="List of stock class conversion rights possible for this stock class"
            ),
        ]
    ] = None
    liquidation_preference_multiple: Optional[
        Annotated[
            Numeric,
            Field(
                description="The liquidation preference per share for this stock class"
            ),
        ]
    ] = None
    participation_cap_multiple: Optional[
        Annotated[
            Numeric,
            Field(
                description="The participation cap multiple per share for this stock class"
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
