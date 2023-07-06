"""Describes how a security converts into a fixed amount of a stock class"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/types/conversion_mechanisms/FixedAmountConversionMechanism.sch
# ema.json

from pydantic import Field
from pyocf.primitives.types.conversion_mechanisms.conversionmechanism import (
    ConversionMechanism,
)
from pyocf.types.numeric import Numeric
from typing import Annotated
from typing import Literal


class FixedAmountConversionMechanism(ConversionMechanism):
    """Describes how a security converts into a fixed amount of a stock class"""

    type: Annotated[
        Literal["FIXED_AMOUNT_CONVERSION"], Field(description="")
    ] = "FIXED_AMOUNT_CONVERSION"
    converts_to_quantity: Annotated[
        Numeric,
        Field(
            description="How many shares of target Stock Class does this security convert into?"
        ),
    ]
