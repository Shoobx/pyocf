"""Type representation of a termination window"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/types/TerminationWindow.schema.json

from pydantic import BaseModel
from pydantic import Field
from pyocf.enums.periodtype import PeriodType
from pyocf.enums.terminationwindowtype import TerminationWindowType
from typing import Annotated


class TerminationWindow(BaseModel):
    """Type representation of a termination window"""

    reason: Annotated[
        TerminationWindowType,
        Field(description="What cause of termination is this window for?"),
    ]
    period: Annotated[
        int,
        Field(
            description="The length of the period in this termination window (in number of periods of"
            "type period_type)"
        ),
    ]
    period_type: Annotated[
        PeriodType,
        Field(description="The type of period being measured (e.g. days or month)"),
    ]
