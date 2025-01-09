"""Enumeration of different OCF file types which are used to load proper schemas
for validation"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.1.0/schema/enums/FileType.schema.json

from enum import Enum


class FileType(Enum):
    """Enumeration of different OCF file types which are used to load proper schemas
    for validation
    """

    ENUM_OCF_MANIFEST_FILE = "OCF_MANIFEST_FILE"
    ENUM_OCF_STAKEHOLDERS_FILE = "OCF_STAKEHOLDERS_FILE"
    ENUM_OCF_STOCK_CLASSES_FILE = "OCF_STOCK_CLASSES_FILE"
    ENUM_OCF_STOCK_LEGEND_TEMPLATES_FILE = "OCF_STOCK_LEGEND_TEMPLATES_FILE"
    ENUM_OCF_STOCK_PLANS_FILE = "OCF_STOCK_PLANS_FILE"
    ENUM_OCF_TRANSACTIONS_FILE = "OCF_TRANSACTIONS_FILE"
    ENUM_OCF_VALUATIONS_FILE = "OCF_VALUATIONS_FILE"
    ENUM_OCF_VESTING_TERMS_FILE = "OCF_VESTING_TERMS_FILE"
