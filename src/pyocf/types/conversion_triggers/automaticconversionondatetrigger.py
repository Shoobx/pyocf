"""Type representation of an automatic trigger on a date."""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/types/conversion_triggers/AutomaticConversionOnDateTrigger.sch
# ema.json

from pydantic import Field
from pyocf.primitives.types.conversion_triggers.conversiontrigger import (
    ConversionTrigger,
)
from pyocf.types.conversion_rights.convertibleconversionright import (
    ConvertibleConversionRight,
)
from pyocf.types.conversion_rights.stockclassconversionright import (
    StockClassConversionRight,
)
from pyocf.types.conversion_rights.warrantconversionright import WarrantConversionRight
from pyocf.types.date import Date
from typing import Annotated
from typing import Literal
from typing import Optional
from typing import Union


class AutomaticConversionOnDateTrigger(ConversionTrigger):
    """Type representation of an automatic trigger on a date."""

    trigger_date: Annotated[
        Date,
        Field(
            description="Date on which trigger occurs automatically (if it hasn't already occured)"
        ),
    ]
    trigger_id: Annotated[
        str,
        Field(
            description="Id for this conversion trigger, unique within list of ConversionTriggers in"
            "parent convertible issuance's `conversion_triggers` field."
        ),
    ]
    nickname: Optional[
        Annotated[
            str,
            Field(
                description="Human-friendly nickname to describe the conversion right"
            ),
        ]
    ] = None
    trigger_description: Optional[
        Annotated[str, Field(description="Long-form description of the trigger")]
    ] = None
    type: Annotated[
        Literal["AUTOMATIC_ON_DATE"], Field(description="")
    ] = "AUTOMATIC_ON_DATE"
    conversion_right: Annotated[
        Union[
            ConvertibleConversionRight,
            WarrantConversionRight,
            StockClassConversionRight,
        ],
        Field(
            discriminator="type",
            description="When the conditions of the trigger are met, how does the convertible convert?",
        ),
    ]
