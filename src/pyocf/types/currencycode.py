"""Type representation of an ISO 4217 currency code"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.1.0/schema/types/CurrencyCode.schema.json

from pydantic import constr
from pyocf.simplebase import SimpleBaseModel


class CurrencyCode(SimpleBaseModel):
    """Type representation of an ISO 4217 currency code"""

    root: constr(pattern=r"^[A-Z]{3}$")
