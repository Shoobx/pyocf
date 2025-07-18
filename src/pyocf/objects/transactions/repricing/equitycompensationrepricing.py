"""Object describing an event that adjusts the exercise price of existing equity
compensation, typically done when the current share price falls significantly
below the set exercise price, rendering an option underwater."""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/main/schema/objects/transactions/repricing/EquityCompensationRepricing.schem
# a.json

from pydantic import Field
from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from pyocf.types.monetary import Monetary
from typing import Annotated
from typing import Literal
from typing import Optional


class EquityCompensationRepricing(Object, Transaction, SecurityTransaction):
    """Object describing an event that adjusts the exercise price of existing equity
    compensation, typically done when the current share price falls significantly
    below the set exercise price, rendering an option underwater.
    """

    object_type: Annotated[
        Literal["TX_EQUITY_COMPENSATION_REPRICING"], Field(description="")
    ] = "TX_EQUITY_COMPENSATION_REPRICING"
    id: Annotated[str, Field(description="Identifier for the object")]
    comments: Optional[
        Annotated[
            list[str],
            Field(
                description="Unstructured text comments related to and stored for the object"
            ),
        ]
    ] = None
    date: Annotated[Date, Field(description="Date on which the transaction occurred")]
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
    new_exercise_price: Annotated[
        Monetary,
        Field(
            description="What is the exercise price of the option after the repricing?"
        ),
    ]
