# Copyright © 2023 FMR LLC

import pytest
import pydantic

from pyocf.api import StakeholderType
from pyocf.api import StakeholdersFile
from pyocf.api import Stakeholder
from pyocf.api import Name, Phone, CountryCode


def test_basic_loading():
    shdata = {
        "object_type": "STAKEHOLDER",
        "id": "d6c49a5a-257d-4b41-9f1d-073a77dfe719",
        "name": {"legal_name": "Person Y"},
        "stakeholder_type": "INDIVIDUAL",
        "comments": [],
    }

    sh = Stakeholder(**shdata)

    assert sh.id == "d6c49a5a-257d-4b41-9f1d-073a77dfe719"
    assert sh.object_type == "STAKEHOLDER"
    assert isinstance(sh.name, Name)
    assert sh.stakeholder_type == StakeholderType.ENUM_INDIVIDUAL
    assert sh.stakeholder_type.value == "INDIVIDUAL"
    assert sh.comments == []
    assert sh.issuer_assigned_id is None
    assert sh.current_relationship is None
    assert sh.primary_contact is None
    assert sh.addresses is None
    assert sh.tax_ids is None


def test_fails():
    shdata = {
        "object_type": "STAKEHOLDER",
        "id": "d6c49a5a-257d-4b41-9f1d-073a77dfe719",
        "name": {"first_name": "Person Y"},
        "stakeholder_type": "INDIVIDUAL",
        "comments": [],
    }

    with pytest.raises(pydantic.ValidationError):
        Stakeholder(**shdata)

    shdata = {
        "object_type": "STAKEHOLDER",
        "id": "d6c49a5a-257d-4b41-9f1d-073a77dfe719",
        "name": {"legal_name": "Person Y"},
        "stakeholder_type": "ELECTRIC GUITAR",
        "comments": [],
    }

    with pytest.raises(pydantic.ValidationError):
        Stakeholder(**shdata)


def test_minimal():
    # "const" are Literals and also defaults. They are required,
    # but you don't have to pass them in.
    sh = StakeholdersFile(items=[])
    assert sh.file_type == "OCF_STAKEHOLDERS_FILE"


def test_constrained_strings():
    # Phone numbers must be phone numbers:
    Phone(phone_type="HOME", phone_number="+1 555 123 4567")

    with pytest.raises(ValueError):
        Phone(phone_type="HOME", phone_number="It's a pizza")

    # Many types uses a root validator, test that:
    CountryCode("SE")

    with pytest.raises(ValueError):
        CountryCode("S2")

    with pytest.raises(ValueError):
        CountryCode("SPUT")
