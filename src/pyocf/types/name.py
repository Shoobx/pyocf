"""Type comprising of multiple name components"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/types/Name.schema.json

from pydantic import BaseModel
from pydantic import Field
from typing import Annotated
from typing import Optional


class Name(BaseModel):
    """Type comprising of multiple name components"""

    legal_name: Annotated[
        str, Field(description="Legal full name for the individual/institution")
    ]
    first_name: Optional[
        Annotated[str, Field(description="First/given name for the individual")]
    ] = None
    last_name: Optional[
        Annotated[str, Field(description="Last/family name for the individual")]
    ] = None
