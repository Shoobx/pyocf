"""Type representation of a government identifier for tax purposes (e.g. EIN) and
corresponding country code (ISO-3166)"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.1.0/schema/types/TaxID.schema.json

from pydantic import BaseModel
from pydantic import Field
from pyocf.types.countrycode import CountryCode
from typing import Annotated


class TaxID(BaseModel):
    """Type representation of a government identifier for tax purposes (e.g. EIN) and
    corresponding country code (ISO-3166)
    """

    tax_id: Annotated[str, Field(description="Tax identifier as string")]
    country: Annotated[
        CountryCode,
        Field(
            description="Issuing country code (ISO 3166-1 alpha-2) for the tax identifier"
        ),
    ]
