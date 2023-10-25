"""Object describing warrant issuance transaction by the issuer and held by a
stakeholder"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.0.0/schema/objects/transactions/issuance/WarrantIssuance.schema.json

from pydantic import Field
from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.issuance.issuance import Issuance
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.conversion_triggers.automaticconversiononconditiontrigger import (
    AutomaticConversionOnConditionTrigger,
)
from pyocf.types.conversion_triggers.automaticconversionondatetrigger import (
    AutomaticConversionOnDateTrigger,
)
from pyocf.types.conversion_triggers.electiveconversionatwilltrigger import (
    ElectiveConversionAtWillTrigger,
)
from pyocf.types.conversion_triggers.electiveconversionindaterangetrigger import (
    ElectiveConversionInDateRangeTrigger,
)
from pyocf.types.conversion_triggers.electiveconversiononconditiontrigger import (
    ElectiveConversionOnConditionTrigger,
)
from pyocf.types.conversion_triggers.unspecifiedconversiontrigger import (
    UnspecifiedConversionTrigger,
)
from pyocf.types.date import Date
from pyocf.types.monetary import Monetary
from pyocf.types.numeric import Numeric
from pyocf.types.securityexemption import SecurityExemption
from typing import Annotated
from typing import Literal
from typing import Optional
from typing import Union


class WarrantIssuance(Object, Transaction, SecurityTransaction, Issuance):
    """Object describing warrant issuance transaction by the issuer and held by a
    stakeholder
    """

    object_type: Annotated[
        Literal["TX_WARRANT_ISSUANCE"], Field(description="")
    ] = "TX_WARRANT_ISSUANCE"
    quantity: Annotated[
        Numeric, Field(description="Quantity of shares the warrant is exercisable for")
    ]
    exercise_price: Annotated[
        Monetary, Field(description="The exercise price of the warrant")
    ]
    purchase_price: Annotated[
        Monetary,
        Field(
            description="Actual purchase price of the warrant (sum up purported value of all"
            "consideration, including in-kind)"
        ),
    ]
    exercise_triggers: Annotated[
        list[
            Annotated[
                Union[
                    AutomaticConversionOnConditionTrigger,
                    AutomaticConversionOnDateTrigger,
                    ElectiveConversionAtWillTrigger,
                    ElectiveConversionInDateRangeTrigger,
                    ElectiveConversionOnConditionTrigger,
                    UnspecifiedConversionTrigger,
                ],
                Field(discriminator="type"),
            ]
        ],
        Field(
            description="In event the Warrant can convert due to trigger events (e.g. Maturity, Next"
            "Qualified Financing, Change of Control, at Election of Holder), what are the"
            "terms?"
        ),
    ]
    warrant_expiration_date: Optional[
        Annotated[
            Date,
            Field(description="What is expiration date of the warrant (if applicable)"),
        ]
    ] = None
    vesting_terms_id: Optional[
        Annotated[
            str,
            Field(
                description="Identifier of the VestingTerms to which this security is subject. If not"
                "present, security is fully vested on issuance."
            ),
        ]
    ] = None
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
    custom_id: Annotated[
        str, Field(description="A custom ID for this security (e.g. CN-1.)")
    ]
    stakeholder_id: Annotated[
        str,
        Field(
            description="Identifier for the stakeholder that holds legal title to this security"
        ),
    ]
    board_approval_date: Optional[
        Annotated[Date, Field(description="Date of board approval for the security")]
    ] = None
    consideration_text: Optional[
        Annotated[
            str,
            Field(
                description="Unstructured text description of consideration provided in exchange for security"
                "issuance"
            ),
        ]
    ] = None
    security_law_exemptions: Annotated[
        list[SecurityExemption],
        Field(
            description="List of security law exemptions (and applicable jurisdictions) for this security"
        ),
    ]
