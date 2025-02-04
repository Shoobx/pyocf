"""Describes a vesting condition satisfied when a period of time, relative to
another vesting condition, has elapsed."""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/types/vesting/VestingScheduleRelativeTrigger.schema.json

from pydantic import Field
from pyocf.primitives.types.vesting.vestingconditiontrigger import (
    VestingConditionTrigger,
)
from pyocf.types.vesting.vestingperiodindays import VestingPeriodInDays
from pyocf.types.vesting.vestingperiodinmonths import VestingPeriodInMonths
from typing import Annotated
from typing import Literal
from typing import Union


class VestingScheduleRelativeTrigger(VestingConditionTrigger):
    """Describes a vesting condition satisfied when a period of time, relative to
    another vesting condition, has elapsed.
    """

    type: Annotated[Literal["VESTING_SCHEDULE_RELATIVE"], Field(description="")] = (
        "VESTING_SCHEDULE_RELATIVE"
    )
    period: Annotated[
        Union[VestingPeriodInDays, VestingPeriodInMonths],
        Field(
            discriminator="type",
            description="The span of time that must have elapsed since the condition"
            "`relative_to_condition_id` occurred for this condition to trigger. For weeks or"
            '"ideal" years (365 days), use `VestingPeriodInDays`. For calendar years use'
            "`VestingPeriodInMonths`.",
        ),
    ]
    relative_to_condition_id: Annotated[
        str,
        Field(
            description="Reference to the vesting condition ID to which the `period` is relative"
        ),
    ]
