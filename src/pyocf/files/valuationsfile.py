"""JSON containing file type identifier and list of valuations"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/files/ValuationsFile.schema.json

from pydantic import Field
from pyocf.objects.valuation import Valuation
from pyocf.primitives.files.file import FileObject
from typing import Annotated
from typing import Literal


class ValuationsFile(FileObject):
    """JSON containing file type identifier and list of valuations"""

    items: Annotated[
        list[Valuation], Field(description="List of OCF valuation objects")
    ]
    file_type: Annotated[Literal["OCF_VALUATIONS_FILE"], Field(description="")] = (
        "OCF_VALUATIONS_FILE"
    )
