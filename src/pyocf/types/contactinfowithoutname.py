"""Type representation of the contact info for an individual stakeholder"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.1.0/schema/types/ContactInfoWithoutName.schema.json

from pydantic import BaseModel
from pydantic import Field
from pyocf.types.email import Email
from pyocf.types.phone import Phone
from typing import Annotated
from typing import Optional


class ContactInfoWithoutName(BaseModel):
    """Type representation of the contact info for an individual stakeholder"""

    phone_numbers: Optional[
        Annotated[
            list[Phone], Field(description="Phone numbers to reach the contact at")
        ]
    ] = None
    emails: Optional[
        Annotated[list[Email], Field(description="Emails to reach the contact at")]
    ] = None
