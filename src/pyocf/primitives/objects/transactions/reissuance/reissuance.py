"""Abstract object describing common properties to a reissuance of a security"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/primitives/objects/transactions/reissuance/Reissuance.schema.j
# son

from pydantic import BaseModel
from pydantic import Field
from typing import Annotated
from typing import Optional


class Reissuance(BaseModel):
    """Abstract object describing common properties to a reissuance of a security"""

    resulting_security_ids: Annotated[
        list[str],
        Field(
            description="Identifier of the new security (or securities) issuance resulting from a"
            "reissuance"
        ),
    ]
    split_transaction_id: Optional[
        Annotated[
            str,
            Field(
                description="When stock is reissued as a result of a stock split, this field contains id of"
                "the respective stock class split transaction. It is not set otherwise."
            ),
        ]
    ]
    reason_text: Optional[
        Annotated[
            str,
            Field(description="Free-form human-readable reason for stock reissuance"),
        ]
    ]
