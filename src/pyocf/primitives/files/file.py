"""Abstract file to be extended by all other files"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/primitives/files/File.schema.json

from pydantic import BaseModel
from pydantic import Field
from pyocf.enums.filetype import FileType
from typing import Annotated


class FileObject(BaseModel):
    """Abstract file to be extended by all other files"""

    file_type: Annotated[
        FileType,
        Field(
            description="File type field (used to select proper schema for validation)"
        ),
    ]
