"""Abstract transaction object to be extended by all transaction objects that
affect a stock plan"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.1.0/schema/primitives/objects/transactions/StockPlanTransaction.schema.js
# on

from pydantic import BaseModel
from pydantic import Field
from typing import Annotated


class StockPlanTransaction(BaseModel):
    """Abstract transaction object to be extended by all transaction objects that
    affect a stock plan
    """

    stock_plan_id: Annotated[
        str,
        Field(
            description="Identifier of the Stock Plan object, a subject of this transaction"
        ),
    ]
