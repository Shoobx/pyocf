"""Describes a period of time expressed in days (e.g. 365 days) for use in Vesting
Terms"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/types/vesting/VestingPeriodInDays.schema.json

from pydantic import Field
from pyocf.primitives.types.vesting.vestingperiod import VestingPeriod
from typing import Annotated
from typing import Literal


class VestingPeriodInDays(VestingPeriod):
    """Describes a period of time expressed in days (e.g. 365 days) for use in Vesting
    Terms
    """

    length: Annotated[
        int,
        Field(
            description="The quantity of `type` units of time; e.g. for 3 months, this would be `3`; for"
            "30 days, this would be `30`"
        ),
    ]
    type: Annotated[Literal["DAYS"], Field(description="")] = "DAYS"
    occurrences: Annotated[
        int,
        Field(
            description="The number of times this vesting period triggers. If vesting occurs monthly for"
            "36 months, for example, this would be `36`"
        ),
    ]
