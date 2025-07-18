"""Type representation of a securities issuance exemption that includes an
unstructured description and a country code for ease of processing and analysis"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/types/SecurityExemption.schema.json

from pydantic import BaseModel
from pydantic import Field
from typing import Annotated


class SecurityExemption(BaseModel):
    """Type representation of a securities issuance exemption that includes an
    unstructured description and a country code for ease of processing and analysis
    """

    description: Annotated[
        str,
        Field(
            description="Description of an applicable security law exemption governing the issuance"
        ),
    ]
    jurisdiction: Annotated[
        str,
        Field(
            description="Jurisdiction of the applicable law. This is a free-text field as there is no"
            "known enumeration of all global legal jurisdictions, but please try to use ISO"
            "3166-1 alpha-2, if appropriate. Otherwise, we rely on implementers to choose an"
            "appropriate value here."
        ),
    ]
