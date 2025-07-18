"""Enumeration of parent sources a stock can be issued or created from"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/enums/ParentSecurityType.schema.json

from enum import Enum


class ParentSecurityType(Enum):
    """Enumeration of parent sources a stock can be issued or created from"""

    ENUM_STOCK_PLAN = "STOCK_PLAN"
    ENUM_STOCK = "STOCK"
    ENUM_WARRANT = "WARRANT"
    ENUM_CONVERTIBLE = "CONVERTIBLE"
