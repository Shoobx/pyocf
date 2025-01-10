"""Object for a plan security exercise (which is a compatibility wrapper for Equity
Compensation Exercise)"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.2.0/schema/objects/transactions/exercise/PlanSecurityExercise.schema.json

from pydantic import Field
from pyocf.objects.transactions.exercise.equitycompensationexercise import (
    EquityCompensationExercise,
)
from typing import Annotated
from typing import Literal


class PlanSecurityExercise(EquityCompensationExercise):
    """Object for a plan security exercise (which is a compatibility wrapper for Equity
    Compensation Exercise)
    """

    object_type: Annotated[
        Literal["TX_PLAN_SECURITY_EXERCISE"], Field(description="")
    ] = "TX_PLAN_SECURITY_EXERCISE"
