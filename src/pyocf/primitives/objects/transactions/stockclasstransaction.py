"""Abstract transaction object to be extended by all transaction objects that
affect the stock class"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.2.0/schema/primitives/objects/transactions/StockClassTransaction.schema.j
# son

from pydantic import BaseModel
from pydantic import Field
from typing import Annotated


class StockClassTransaction(BaseModel):
    """Abstract transaction object to be extended by all transaction objects that
    affect the stock class
    """

    stock_class_id: Annotated[
        str,
        Field(
            description="Identifier of the StockClass object, a subject of this transaction"
        ),
    ]
