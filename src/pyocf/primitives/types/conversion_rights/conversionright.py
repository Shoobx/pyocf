"""Abstract type representation of a conversion right from a non-plan security into
another non-plan security"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.2.0/schema/primitives/types/conversion_rights/ConversionRight.schema.json

from pydantic import BaseModel
from pydantic import Field
from pyocf.enums.conversionrighttype import ConversionRightType
from pyocf.types.conversion_mechanisms.customconversionmechanism import (
    CustomConversionMechanism,
)
from pyocf.types.conversion_mechanisms.fixedamountconversionmechanism import (
    FixedAmountConversionMechanism,
)
from pyocf.types.conversion_mechanisms.noteconversionmechanism import (
    NoteConversionMechanism,
)
from pyocf.types.conversion_mechanisms.percentcapitalizationconversionmechanism import (
    PercentCapitalizationConversionMechanism,
)
from pyocf.types.conversion_mechanisms.ratioconversionmechanism import (
    RatioConversionMechanism,
)
from pyocf.types.conversion_mechanisms.safeconversionmechanism import (
    SAFEConversionMechanism,
)
from pyocf.types.conversion_mechanisms.sharepricebasedconversionmechanism import (
    SharePriceBasedConversionMechanism,
)
from pyocf.types.conversion_mechanisms.valuationbasedconversionmechanism import (
    ValuationBasedConversionMechanism,
)
from typing import Annotated
from typing import Optional
from typing import Union


class ConversionRight(BaseModel):
    """Abstract type representation of a conversion right from a non-plan security into
    another non-plan security
    """

    type: Optional[
        Annotated[
            ConversionRightType,
            Field(description="What kind of conversion right is this?"),
        ]
    ] = None
    conversion_mechanism: Annotated[
        Union[
            SAFEConversionMechanism,
            NoteConversionMechanism,
            CustomConversionMechanism,
            PercentCapitalizationConversionMechanism,
            FixedAmountConversionMechanism,
            RatioConversionMechanism,
            ValuationBasedConversionMechanism,
            SharePriceBasedConversionMechanism,
        ],
        Field(
            discriminator="type",
            description="What conversion mechanism applies to calculate the number of resulting"
            "securities?",
        ),
    ]
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
