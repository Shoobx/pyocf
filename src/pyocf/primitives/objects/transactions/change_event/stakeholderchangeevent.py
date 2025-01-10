"""Abstract change event \"transaction\" object to be extended by all change event
\"transaction\" objects that affect a stakeholder"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/main/schema/primitives/objects/transactions/change_event/StakeholderChangeEv
# ent.schema.json

from pydantic import BaseModel
from pydantic import Field
from typing import Annotated


class StakeholderChangeEvent(BaseModel):
    """Abstract change event \"transaction\" object to be extended by all change event
    \"transaction\" objects that affect a stakeholder
    """

    stakeholder_id: Annotated[
        str,
        Field(
            description="Identifier of the Stakeholder object, a subject of this change event"
            '"transaction"'
        ),
    ]