"""Type representation of a phone number"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.0.0/schema/types/Phone.schema.json

from pydantic import BaseModel
from pydantic import Field
from pydantic import constr
from pyocf.enums.phonetype import PhoneType
from typing import Annotated


class Phone(BaseModel):
    """Type representation of a phone number"""

    phone_type: Annotated[
        PhoneType,
        Field(description="Type of phone number (e.g. mobile, home or business)"),
    ]
    phone_number: Annotated[
        constr(pattern=r"^\+\d{1,3}\s\d{2,3}\s\d{2,3}\s\d{4}$"),
        Field(
            description="A valid phone number string in ITU E.123 international notation (e.g. +123 123"
            "456 7890)"
        ),
    ]
