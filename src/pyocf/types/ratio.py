"""Type representation of a ratio as two parts of a quotient, i.e. numerator and"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.0.0/schema/types/Ratio.schema.json

from pydantic import BaseModel
from pyocf.types.numeric import Numeric


class Ratio(BaseModel):
    """Type representation of a ratio as two parts of a quotient, i.e. numerator and
    denominator numeric values
    """

    # Numerator of the ratio, i.e. the ratio of A to B (A:B) can be expressed as a
    # fraction (A/B), where A is the numerator
    numerator: Numeric
    # Denominator of the ratio, i.e. the ratio of A to B (A:B) can be expressed as a
    # fraction (A/B), where B is the denominator
    denominator: Numeric
