"""JSON containing file type identifier and list of stock classes"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/files/StockClassesFile.schema.json

from pydantic import Field
from pyocf.objects.stockclass import StockClass
from pyocf.primitives.files.file import FileObject
from typing import Annotated
from typing import Literal


class StockClassesFile(FileObject):
    """JSON containing file type identifier and list of stock classes"""

    items: Annotated[
        list[StockClass], Field(description="List of OCF stock class objects")
    ]
    file_type: Annotated[Literal["OCF_STOCK_CLASSES_FILE"], Field(description="")] = (
        "OCF_STOCK_CLASSES_FILE"
    )
