"""Type representation of an email address"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/types/Email.schema.json

from pydantic import BaseModel
from pydantic import Field
from pyocf.enums.emailtype import EmailType
from typing import Annotated


class Email(BaseModel):
    """Type representation of an email address"""

    email_type: Annotated[
        EmailType,
        Field(description="Type of e-mail address (e.g. personal or business)"),
    ]
    email_address: Annotated[str, Field(description="A valid e-mail address")]
