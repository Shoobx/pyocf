"""Enumeration types of valuation inputs that go into a formula - e.g. use a
specified value (`FIXED`), a cap (`VALUATION_CAP`) or actual valuation
(`ACTUAL`)."""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/enums/ValuationBasedFormulaType.schema.json

from enum import Enum


class ValuationBasedFormulaType(Enum):
    """Enumeration types of valuation inputs that go into a formula - e.g. use a
    specified value (`FIXED`), a cap (`VALUATION_CAP`) or actual valuation
    (`ACTUAL`).
    """

    ENUM_FIXED = "FIXED"
    ENUM_ACTUAL = "ACTUAL"
    ENUM_CAP = "CAP"