"""Abstract type setting forth required field(s) for ALL conversion mechanism types"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/primitives/types/conversion_mechanisms/ConversionMechanism.sch
# ema.json

from pydantic import BaseModel
from pyocf.enums.conversionmechanismtype import ConversionMechanismType


class ConversionMechanism(BaseModel):
    """Abstract type setting forth required field(s) for ALL conversion mechanism types"""

    # Identifies the specific conversion trigger type
    type: ConversionMechanismType
