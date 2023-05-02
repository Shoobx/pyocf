"""Abstract object describing fields common to all conversion transaction objects"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/primitives/objects/transactions/conversion/Conversion.schema.j
# son

from pydantic import BaseModel


class Conversion(BaseModel):
    """Abstract object describing fields common to all conversion transaction objects"""

    # Identifier for the security (or securities) that resulted from the conversion
    resulting_security_ids: list[str]
