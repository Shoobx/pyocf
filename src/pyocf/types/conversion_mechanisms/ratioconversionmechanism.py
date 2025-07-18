"""Sets forth inputs and conversion mechanism of a ratio conversion (primarily used
to describe conversion from one stock class (e.g. Preferred) into another (e.g.
Common)"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.2.0/schema/types/conversion_mechanisms/RatioConversionMechanism.schema.js
# on

from pydantic import Field
from pyocf.enums.roundingtype import RoundingType
from pyocf.primitives.types.conversion_mechanisms.conversionmechanism import (
    ConversionMechanism,
)
from pyocf.types.monetary import Monetary
from pyocf.types.ratio import Ratio
from typing import Annotated
from typing import Literal


class RatioConversionMechanism(ConversionMechanism):
    """Sets forth inputs and conversion mechanism of a ratio conversion (primarily used
    to describe conversion from one stock class (e.g. Preferred) into another (e.g.
    Common)
    """

    type: Annotated[Literal["RATIO_CONVERSION"], Field(description="")] = (
        "RATIO_CONVERSION"
    )
    conversion_price: Annotated[
        Monetary,
        Field(
            description="What is the effective conversion price per share of this stock class?"
        ),
    ]
    ratio: Annotated[
        Ratio,
        Field(
            description="One share of this stock class converts into this many target stock class shares"
        ),
    ]
    rounding_type: Annotated[
        RoundingType, Field(description="How should fractional shares be rounded?")
    ]
