"""For a given stock plan, what is the default rule for what happens to the shares
reserved for a Plan Security after it\'s cancelled."""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/enums/StockPlanCancellationBehaviorType.schema.json

from enum import Enum


class StockPlanCancellationBehaviorType(Enum):
    """For a given stock plan, what is the default rule for what happens to the shares
    reserved for a Plan Security after it\'s cancelled.
    """

    ENUM_RETIRE = "RETIRE"
    ENUM_RETURN_TO_POOL = "RETURN_TO_POOL"
    ENUM_HOLD_AS_CAPITAL_STOCK = "HOLD_AS_CAPITAL_STOCK"
    ENUM_DEFINED_PER_PLAN_SECURITY = "DEFINED_PER_PLAN_SECURITY"
