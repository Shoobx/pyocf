"""Type representation of a ratio as two parts of a quotient, i.e. numerator and
denominator numeric values"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/types/Ratio.schema.json

from pydantic import BaseModel
from pydantic import Field
from pyocf.types.numeric import Numeric
from typing import Annotated


class Ratio(BaseModel):
    """Type representation of a ratio as two parts of a quotient, i.e. numerator and
    denominator numeric values
    """

    numerator: Annotated[
        Numeric,
        Field(
            description="Numerator of the ratio, i.e. the ratio of A to B (A:B) can be expressed as a"
            "fraction (A/B), where A is the numerator"
        ),
    ]
    denominator: Annotated[
        Numeric,
        Field(
            description="Denominator of the ratio, i.e. the ratio of A to B (A:B) can be expressed as a"
            "fraction (A/B), where B is the denominator"
        ),
    ]
