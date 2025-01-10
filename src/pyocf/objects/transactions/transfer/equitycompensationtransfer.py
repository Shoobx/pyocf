"""Object describing a transfer of equity compensation"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.2.0/schema/objects/transactions/transfer/EquityCompensationTransfer.schem
# a.json

from pydantic import Field
from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.primitives.objects.transactions.transfer.transfer import Transfer
from pyocf.types.date import Date
from pyocf.types.numeric import Numeric
from typing import Annotated
from typing import Literal
from typing import Optional


class EquityCompensationTransfer(Object, Transaction, SecurityTransaction, Transfer):
    """Object describing a transfer of equity compensation"""

    object_type: Annotated[
        Literal["TX_EQUITY_COMPENSATION_TRANSFER"],
        Field(
            description="This is done to avoid a breaking change as we work towards a bigger restructure"
            "of the equity types in v2.0.0. `TX_PLAN_SECURITY_TRANSFER` will be deprecated in"
            "v2.0.0"
        ),
    ] = "TX_EQUITY_COMPENSATION_TRANSFER"
    quantity: Annotated[
        Numeric,
        Field(description="Quantity of non-monetary security units transferred"),
    ]
    id: Annotated[str, Field(description="Identifier for the object")]
    comments: Optional[
        Annotated[
            list[str],
            Field(
                description="Unstructured text comments related to and stored for the object"
            ),
        ]
    ] = None
    security_id: Annotated[
        str,
        Field(
            description="Identifier for the security (stock, plan security, warrant, or convertible) by"
            "which it can be referenced by other transaction objects. Note that while this"
            "identifier is created with an issuance object, it should be different than the"
            "issuance object's `id` field which identifies the issuance transaction object"
            "itself. All future transactions on the security (e.g. acceptance, transfer,"
            "cancel, etc.) must reference this `security_id` to qualify which security the"
            "transaction applies to."
        ),
    ]
    date: Annotated[Date, Field(description="Date on which the transaction occurred")]
    consideration_text: Optional[
        Annotated[
            str,
            Field(
                description="Unstructured text description of consideration provided in exchange for security"
                "transfer"
            ),
        ]
    ] = None
    balance_security_id: Optional[
        Annotated[
            str,
            Field(
                description="Identifier for the security that holds the remainder balance (for partial"
                "transfers)"
            ),
        ]
    ] = None
    resulting_security_ids: Annotated[
        list[str],
        Field(
            description="Array of identifiers for new security (or securities) created as a result of the"
            "transaction"
        ),
    ]
