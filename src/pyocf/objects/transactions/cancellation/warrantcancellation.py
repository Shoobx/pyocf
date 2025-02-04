"""Object describing a cancellation of a warrant security"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.2.0/schema/objects/transactions/cancellation/WarrantCancellation.schema.j
# son

from pydantic import Field
from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.cancellation.cancellation import Cancellation
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from pyocf.types.numeric import Numeric
from typing import Annotated
from typing import Literal
from typing import Optional


class WarrantCancellation(Object, Transaction, SecurityTransaction, Cancellation):
    """Object describing a cancellation of a warrant security"""

    object_type: Annotated[
        Literal["TX_WARRANT_CANCELLATION"], Field(description="")
    ] = "TX_WARRANT_CANCELLATION"
    quantity: Annotated[
        Numeric, Field(description="Quantity of non-monetary security units cancelled")
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
    balance_security_id: Optional[
        Annotated[
            str,
            Field(
                description="Identifier for the security that holds the remainder balance (for partial"
                "cancellations)"
            ),
        ]
    ] = None
    reason_text: Annotated[str, Field(description="Reason for the cancellation")]
