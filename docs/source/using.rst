Using
=====

Save a captable to a file
-------------------------

To save a captable, you create a Captable object, and fill the various lists
with information:

* ``captable.stakeholders``: A list of all ``Stakeholder`` objects.
* ``captable.stock_classes``: A list of all ``StockClass`` objects.
* ``captable.stock_legend_templates``: A list of all ``StockLegendTemplate`` objects.
* ``captable.stock_plans``: A list of all ``StockPlan`` objects.
* ``captable.transactions``: A list of all ``Transaction`` objects.
* ``captable.valuations``: A list of all ``Valuation`` objects.
* ``captable.vesting_terms``: A list of all ``VestingTerm`` objects.

All the classes generated are kept in the same hierarchy as the original schema, but for
ease of access, they are also accessible through the ``pyocf.api`` module::

.. doctest::

    >>> from pyocf import api
    >>> api.StockLegendTemplate
    <class 'pyocf.objects.stocklegendtemplate.StockLegendTemplate'>

The ``pyocf.api`` module only contains classes from the OCF schema, supporting classes,
like ``pyocf.captable.Captable()`` are not included there, to clarify the separation
from the schema.

In addition to that, there is a ``captable.manifest`` that holds an ``OCFManifestFile``
object. It will be created automatically when saving if you pass in an ``Issuer`` object
as in this example. You can also create a manifest and set it on the ``Captable`` object,
but you then need to create ``File`` objects for each file, with dummy md5 hashes.

.. doctest::

    >>> from datetime import date, datetime
    >>> from os import path
    >>> from pyocf import captable, api

    >>> cap = captable.Captable()
    >>> cap.stakeholders.append(
    ...     api.Stakeholder(
    ...         object_type="STAKEHOLDER",
    ...         id="d6c49a5a-257d-4b41-9f1d-073a77dfe719",
    ...         name={"legal_name": "Person Y"},
    ...         stakeholder_type="INDIVIDUAL",
    ...         comments=[],
    ...      )
    ... )

    >>> cap.transactions.append(
    ...     api.PlanSecurityIssuance(
    ...             object_type="TX_PLAN_SECURITY_ISSUANCE",
    ...             stock_plan_id="test",
    ...             id="Success OPTION",
    ...             custom_id="test",
    ...             stakeholder_id="test",
    ...             option_grant_type="ISO",
    ...             compensation_type="OPTION",
    ...             quantity=1,
    ...             exercise_price={"amount": 1, "currency": "USD"},
    ...             termination_exercise_windows=[],
    ...             security_id="",
    ...             date="2022-12-12",
    ...             security_law_exemptions=[],
    ...      )
    ... )

And once you have filled in all the lists with all the information, you save
the captable:

.. doctest::

    >>> ocf_issuer = api.Issuer(
    ...     id="pyocf",
    ...     legal_name="pyocf example docs",
    ...     formation_date="2023-01-01",
    ...     country_of_formation="US")
    >>> cap.save(path.join(TEST_DIR, "Captable.ocf.zip"),
    ...     issuer=ocf_issuer,
    ... )


Loading a captable from a file
------------------------------

Open Cap Tables will typically be distributed as zip-files. With ``pyocf``
you load them with the ``load()`` method on the Captable class:

.. doctest::

    >>> cap = captable.Captable.load(path.join(TEST_DIR, "Captable.ocf.zip"))

A captable will then be created and Python objects will be stored in it.

.. doctest::

    >>> cap.manifest.issuer.legal_name
    'pyocf example docs'

    >>> cap.stakeholders  # doctest: +NORMALIZE_WHITESPACE
    [Stakeholder(id='d6c49a5a-257d-4b41-9f1d-073a77dfe719', comments=[],
    object_type='STAKEHOLDER', name=Name(legal_name='Person Y', first_name=None,
    last_name=None), stakeholder_type=<StakeholderType.ENUM_INDIVIDUAL:
    'INDIVIDUAL'>, issuer_assigned_id=None, current_relationship=None,
    primary_contact=None, addresses=None, tax_ids=None),
    Stakeholder(id='d6c49a5a-257d-4b41-9f1d-073a77dfe719', comments=[],
    object_type='STAKEHOLDER', name=Name(legal_name='Person Y', first_name=None,
    last_name=None), stakeholder_type=<StakeholderType.ENUM_INDIVIDUAL:
    'INDIVIDUAL'>, issuer_assigned_id=None, current_relationship=None,
    primary_contact=None, addresses=None, tax_ids=None)]
