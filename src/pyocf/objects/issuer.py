"""Object describing the issuer of the cap table (the company whose cap table this"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.0.0/schema/objects/Issuer.schema.json

from pyocf.primitives.objects.object import Object
from pyocf.types.address import Address
from pyocf.types.countrycode import CountryCode
from pyocf.types.countrysubdivisioncode import CountrySubdivisionCode
from pyocf.types.date import Date
from pyocf.types.email import Email
from pyocf.types.phone import Phone
from pyocf.types.taxid import TaxID
from typing import Literal
from typing import Optional


class Issuer(Object):
    """Object describing the issuer of the cap table (the company whose cap table this
    is)
    """

    object_type: Literal["ISSUER"] = "ISSUER"
    # Legal name of the issuer
    legal_name: str
    # Doing Business As name
    dba: Optional[str]
    # Date of formation
    formation_date: Date
    # The country where the issuer company was legally formed (ISO 3166-1 alpha-2)
    country_of_formation: CountryCode
    # The state, province, or subdivision where the issuer company was legally formed
    country_subdivision_of_formation: Optional[CountrySubdivisionCode]
    # The tax ids for this issuer company
    tax_ids: Optional[list[TaxID]]
    # A work email that the issuer company can be reached at
    email: Optional[Email]
    # A phone number that the issuer company can be reached at
    phone: Optional[Phone]
    # The headquarters address of the issuing company
    address: Optional[Address]
    # Identifier for the object
    id: str
    # Unstructured text comments related to and stored for the object
    comments: Optional[list[str]]
