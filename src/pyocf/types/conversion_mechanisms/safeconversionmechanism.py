"""Sets forth inputs and conversion mechanism of a SAFE (mirrors the flavors and
inputs of the Y Combinator SAFE)"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.2.0/schema/types/conversion_mechanisms/SAFEConversionMechanism.schema.jso
# n

from pydantic import Field
from pyocf.enums.conversiontimingtype import ConversionTimingType
from pyocf.primitives.types.conversion_mechanisms.conversionmechanism import (
    ConversionMechanism,
)
from pyocf.types.capitalizationdefinitionrules import CapitalizationDefinitionRules
from pyocf.types.monetary import Monetary
from pyocf.types.percentage import Percentage
from pyocf.types.ratio import Ratio
from typing import Annotated
from typing import Literal
from typing import Optional


class SAFEConversionMechanism(ConversionMechanism):
    """Sets forth inputs and conversion mechanism of a SAFE (mirrors the flavors and
    inputs of the Y Combinator SAFE)
    """

    type: Annotated[Literal["SAFE_CONVERSION"], Field(description="")] = (
        "SAFE_CONVERSION"
    )
    conversion_discount: Optional[
        Annotated[
            Percentage,
            Field(
                description="What is the percentage discount available upon conversion, if applicable?"
                "(decimal representation - e.g. 0.125 for 12.5%)"
            ),
        ]
    ] = None
    conversion_valuation_cap: Optional[
        Annotated[
            Monetary, Field(description="What is the valuation cap (if applicable)?")
        ]
    ] = None
    exit_multiple: Optional[
        Annotated[
            Ratio,
            Field(
                description="For cash proceeds calculation during a liquidity event."
            ),
        ]
    ] = None
    conversion_mfn: Annotated[bool, Field(description="Is this an MFN flavored SAFE?")]
    conversion_timing: Optional[
        Annotated[
            ConversionTimingType,
            Field(
                description="Should the conversion amount be based on pre or post money capitalization"
            ),
        ]
    ] = None
    capitalization_definition: Optional[
        Annotated[
            str,
            Field(
                description="How is company capitalization defined for purposes of conversion? If possible,"
                "include the legal language from the instrument."
            ),
        ]
    ] = None
    capitalization_definition_rules: Optional[
        Annotated[
            CapitalizationDefinitionRules,
            Field(
                description="The rules for which types of securities would be included in the capitalization"
                "definition."
            ),
        ]
    ] = None
