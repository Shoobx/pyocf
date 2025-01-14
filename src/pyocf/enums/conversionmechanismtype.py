"""Enumeration of convertible conversion calculation types."""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.1.0/schema/enums/ConversionMechanismType.schema.json

from enum import Enum


class ConversionMechanismType(Enum):
    """Enumeration of convertible conversion calculation types."""

    ENUM_FIXED_AMOUNT_CONVERSION = "FIXED_AMOUNT_CONVERSION"
    ENUM_FIXED_PERCENT_OF_CAPITALIZATION_CONVERSION = (
        "FIXED_PERCENT_OF_CAPITALIZATION_CONVERSION"
    )
    ENUM_RATIO_CONVERSION = "RATIO_CONVERSION"
    ENUM_SAFE_CONVERSION = "SAFE_CONVERSION"
    ENUM_CONVERTIBLE_NOTE_CONVERSION = "CONVERTIBLE_NOTE_CONVERSION"
    ENUM_CUSTOM_CONVERSION = "CUSTOM_CONVERSION"
