"""Enumeration representing a vesting \"day of month\". Since not all months have
29, 30, or 31 days, this enum requires those values to also specify an overflow
behavior.
 - `01` - `28` : Day 1, 2... 28 of the month; e.g. `03` means vesting occurs on
the 3rd of the month.
 - `29_OR_LAST_DAY_OF_MONTH` - `31_OR_LAST_DAY_OF_MONTH` : Day 29, 30, or 31 of
the month, defaulting to the last day of the month for shorter months; e.g.
`31_OR_LAST_DAY_OF_MONTH` means monthly vesting occurs on Jan 31, Feb 28/29, Mar
31, Apr 30, etc.
 - `VESTING_START_DAY_OR_LAST_DAY_OF_MONTH` vests on the same day of month as
the day of the `VESTING_START` condition; e.g. if vesting commences on Jan 15
then any vesting will accrue on the 15th of future vesting months. If vesting
commencement occurs on days 29-31, this has the same behavior as the other
`*_LAST_DAY_OF_MONTH` values."""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/enums/VestingDayOfMonth.schema.json

from enum import Enum


class VestingDayOfMonth(Enum):
    """Enumeration representing a vesting \"day of month\". Since not all months have
    29, 30, or 31 days, this enum requires those values to also specify an overflow
    behavior.
     - `01` - `28` : Day 1, 2... 28 of the month; e.g. `03` means vesting occurs on
    the 3rd of the month.
     - `29_OR_LAST_DAY_OF_MONTH` - `31_OR_LAST_DAY_OF_MONTH` : Day 29, 30, or 31 of
    the month, defaulting to the last day of the month for shorter months; e.g.
    `31_OR_LAST_DAY_OF_MONTH` means monthly vesting occurs on Jan 31, Feb 28/29, Mar
    31, Apr 30, etc.
     - `VESTING_START_DAY_OR_LAST_DAY_OF_MONTH` vests on the same day of month as
    the day of the `VESTING_START` condition; e.g. if vesting commences on Jan 15
    then any vesting will accrue on the 15th of future vesting months. If vesting
    commencement occurs on days 29-31, this has the same behavior as the other
    `*_LAST_DAY_OF_MONTH` values.
    """

    ENUM_01 = "01"
    ENUM_02 = "02"
    ENUM_03 = "03"
    ENUM_04 = "04"
    ENUM_05 = "05"
    ENUM_06 = "06"
    ENUM_07 = "07"
    ENUM_08 = "08"
    ENUM_09 = "09"
    ENUM_10 = "10"
    ENUM_11 = "11"
    ENUM_12 = "12"
    ENUM_13 = "13"
    ENUM_14 = "14"
    ENUM_15 = "15"
    ENUM_16 = "16"
    ENUM_17 = "17"
    ENUM_18 = "18"
    ENUM_19 = "19"
    ENUM_20 = "20"
    ENUM_21 = "21"
    ENUM_22 = "22"
    ENUM_23 = "23"
    ENUM_24 = "24"
    ENUM_25 = "25"
    ENUM_26 = "26"
    ENUM_27 = "27"
    ENUM_28 = "28"
    ENUM_29_OR_LAST_DAY_OF_MONTH = "29_OR_LAST_DAY_OF_MONTH"
    ENUM_30_OR_LAST_DAY_OF_MONTH = "30_OR_LAST_DAY_OF_MONTH"
    ENUM_31_OR_LAST_DAY_OF_MONTH = "31_OR_LAST_DAY_OF_MONTH"
    ENUM_VESTING_START_DAY_OR_LAST_DAY_OF_MONTH = (
        "VESTING_START_DAY_OR_LAST_DAY_OF_MONTH"
    )
