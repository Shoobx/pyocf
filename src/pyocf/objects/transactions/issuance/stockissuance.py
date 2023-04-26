"""Object describing a stock issuance transaction by the issuer and held by a"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/main/schema/objects/transactions/issuance/StockIssuance.schema.json

from pyocf.enums.stockissuancetype import StockIssuanceType
from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.issuance.issuance import Issuance
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from pyocf.types.monetary import Monetary
from pyocf.types.numeric import Numeric
from pyocf.types.securityexemption import SecurityExemption
from pyocf.types.sharenumberrange import ShareNumberRange
from typing import Literal
from typing import Optional


class StockIssuance(Object, Transaction, SecurityTransaction, Issuance):
    """Object describing a stock issuance transaction by the issuer and held by a
    stakeholder
    """

    object_type: Literal["TX_STOCK_ISSUANCE"] = "TX_STOCK_ISSUANCE"
    # Identifier of the stock class for this stock issuance
    stock_class_id: str
    # Identifier of StockPlan the Stock was issued from (in the case of RSAs or Stock
    # issued from a plan).
    stock_plan_id: Optional[str]
    # Range(s) of the specific share numbers included in this issuance. This is
    # different from a certificate number you might include in the `custom_id` field
    # or the `security_id` created in this issuance. This field should be used where,
    # for whatever reason, shares are not fungible and you must track, with each
    # issuance, *which* specific share numbers are included in the issuance - e.g.
    # share numbers 1 - 100 and 250-300.
    share_numbers_issued: Optional[list[ShareNumberRange]]
    # The price per share paid for the stock by the holder
    share_price: Monetary
    # Number of shares issued to the stakeholder
    quantity: Numeric
    # Identifier of the VestingTerms to which this security is subject. If not
    # present, security is fully vested on issuance.
    vesting_terms_id: Optional[str]
    # The cost basis for this particular stock
    cost_basis: Optional[Monetary]
    # List of stock legend ids that apply to this stock
    stock_legend_ids: list[str]
    # Optional field to flag certain special types of issuances (like RSAs)
    issuance_type: Optional[StockIssuanceType]
    # Identifier for the object
    id: str
    # Unstructured text comments related to and stored for the object
    comments: Optional[list[str]]
    # Identifier for the security (stock, plan security, warrant, or convertible) by
    # which it can be referenced by other transaction objects. Note that while this
    # identifier is created with an issuance object, it should be different than the
    # issuance object's `id` field which identifies the issuance transaction object
    # itself. All future transactions on the security (e.g. acceptance, transfer,
    # cancel, etc.) must reference this `security_id` to qualify which security the
    # transaction applies to.
    security_id: str
    # Date on which the transaction occurred
    date: Date
    # A custom ID for this security (e.g. CN-1.)
    custom_id: str
    # Identifier for the stakeholder that holds legal title to this security
    stakeholder_id: str
    # Date of board approval for the security
    board_approval_date: Optional[Date]
    # Unstructured text description of consideration provided in exchange for security
    # issuance
    consideration_text: Optional[str]
    # List of security law exemptions (and applicable jurisdictions) for this security
    security_law_exemptions: list[SecurityExemption]
