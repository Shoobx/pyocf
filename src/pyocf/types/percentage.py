"""Fixed-point string representation of a percentage as a decimal between 0.0 and
1.0 (up to 10 decimal places supported)"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.0.0/schema/types/Percentage.schema.json

from pydantic import constr
from pyocf.simplebase import SimpleBaseModel


class Percentage(SimpleBaseModel):
    """Fixed-point string representation of a percentage as a decimal between 0.0 and
    1.0 (up to 10 decimal places supported)
    """

    root: constr(pattern=r"^0?(\.[0-9]{1,10})?$|^1(\.0{1,10})?$")
