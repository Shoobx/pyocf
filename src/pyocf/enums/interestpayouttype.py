"""Enumeration of interest payout types (e.g. deferred or cash payment)"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.0.0/schema/enums/InterestPayoutType.schema.json

from enum import Enum


class InterestPayoutType(Enum):
    """Enumeration of interest payout types (e.g. deferred or cash payment)"""

    ENUM_DEFERRED = "DEFERRED"
    ENUM_CASH = "CASH"
