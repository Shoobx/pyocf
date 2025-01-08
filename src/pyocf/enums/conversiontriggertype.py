"""Enumeration of types of triggers common to various legal rights - e.g. does the
satisfaction of a condition trigger an automatic conversion or merely a right to
convert? If `UNSPECIFIED`, the system of record cannot represent this data in a
structured form."""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.1.0/schema/enums/ConversionTriggerType.schema.json

from enum import Enum


class ConversionTriggerType(Enum):
    """Enumeration of types of triggers common to various legal rights - e.g. does the
    satisfaction of a condition trigger an automatic conversion or merely a right to
    convert? If `UNSPECIFIED`, the system of record cannot represent this data in a
    structured form.
    """

    ENUM_AUTOMATIC_ON_CONDITION = "AUTOMATIC_ON_CONDITION"
    ENUM_AUTOMATIC_ON_DATE = "AUTOMATIC_ON_DATE"
    ENUM_ELECTIVE_IN_RANGE = "ELECTIVE_IN_RANGE"
    ENUM_ELECTIVE_ON_CONDITION = "ELECTIVE_ON_CONDITION"
    ENUM_ELECTIVE_AT_WILL = "ELECTIVE_AT_WILL"
    ENUM_UNSPECIFIED = "UNSPECIFIED"
