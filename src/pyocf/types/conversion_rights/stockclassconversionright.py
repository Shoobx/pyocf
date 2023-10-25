"""Type representation of a conversion right from one Stock Class into another
Stock Class"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/types/conversion_rights/StockClassConversionRight.schema.json

from pydantic import Field
from pyocf.primitives.types.conversion_rights.conversionright import ConversionRight
from pyocf.types.conversion_mechanisms.ratioconversionmechanism import (
    RatioConversionMechanism,
)
from typing import Annotated
from typing import Literal
from typing import Optional


class StockClassConversionRight(ConversionRight):
    """Type representation of a conversion right from one Stock Class into another
    Stock Class
    """

    type: Annotated[
        Literal["STOCK_CLASS_CONVERSION_RIGHT"], Field(description="")
    ] = "STOCK_CLASS_CONVERSION_RIGHT"
    conversion_mechanism: Annotated[RatioConversionMechanism, Field(description="")]
    converts_to_future_round: Optional[
        Annotated[
            bool,
            Field(
                description="Is this stock class potentially convertible into a future, as-yet undetermined"
                "stock class (e.g. Founder Preferred)"
            ),
        ]
    ] = None
    converts_to_stock_class_id: Optional[
        Annotated[
            str,
            Field(
                description="The identifier of the existing, known stock class this stock class can convert"
                "into"
            ),
        ]
    ] = None
