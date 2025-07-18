"""Abstract type setting forth required field(s) for ALL conversion mechanism types"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.2.0/schema/primitives/types/conversion_mechanisms/ConversionMechanism.sch
# ema.json

from pydantic import BaseModel
from pydantic import Field
from pyocf.enums.conversionmechanismtype import ConversionMechanismType
from typing import Annotated


class ConversionMechanism(BaseModel):
    """Abstract type setting forth required field(s) for ALL conversion mechanism types"""

    type: Annotated[
        ConversionMechanismType,
        Field(description="Identifies the specific conversion trigger type"),
    ]
