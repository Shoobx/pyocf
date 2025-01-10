"""An object that represents a plan security acceptance transaction, which is just
a compatibility wrapper for an Equity Compensation Acceptance."""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.2.0/schema/objects/transactions/acceptance/PlanSecurityAcceptance.schema.
# json

from pydantic import Field
from pyocf.objects.transactions.acceptance.equitycompensationacceptance import (
    EquityCompensationAcceptance,
)
from typing import Annotated
from typing import Literal


class PlanSecurityAcceptance(EquityCompensationAcceptance):
    """An object that represents a plan security acceptance transaction, which is just
    a compatibility wrapper for an Equity Compensation Acceptance.
    """

    object_type: Annotated[
        Literal["TX_PLAN_SECURITY_ACCEPTANCE"],
        Field(
            description="This is done to avoid a breaking change as we work towards a bigger restructure"
            "of the equity types in v2.0.0. `TX_PLAN_SECURITY_ACCEPTANCE` will be deprecated"
            "in v2.0.0"
        ),
    ] = "TX_PLAN_SECURITY_ACCEPTANCE"
