"""Enumeration of object types"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2024 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.2.0/schema/enums/ObjectType.schema.json

from enum import Enum


class ObjectType(Enum):
    """Enumeration of object types"""

    ENUM_ISSUER = "ISSUER"
    ENUM_STAKEHOLDER = "STAKEHOLDER"
    ENUM_STOCK_CLASS = "STOCK_CLASS"
    ENUM_STOCK_LEGEND_TEMPLATE = "STOCK_LEGEND_TEMPLATE"
    ENUM_STOCK_PLAN = "STOCK_PLAN"
    ENUM_VALUATION = "VALUATION"
    ENUM_VESTING_TERMS = "VESTING_TERMS"
    ENUM_FINANCING = "FINANCING"
    ENUM_DOCUMENT = "DOCUMENT"
    ENUM_TX_ISSUER_AUTHORIZED_SHARES_ADJUSTMENT = (
        "TX_ISSUER_AUTHORIZED_SHARES_ADJUSTMENT"
    )
    ENUM_TX_STOCK_CLASS_CONVERSION_RATIO_ADJUSTMENT = (
        "TX_STOCK_CLASS_CONVERSION_RATIO_ADJUSTMENT"
    )
    ENUM_TX_STOCK_CLASS_AUTHORIZED_SHARES_ADJUSTMENT = (
        "TX_STOCK_CLASS_AUTHORIZED_SHARES_ADJUSTMENT"
    )
    ENUM_TX_STOCK_CLASS_SPLIT = "TX_STOCK_CLASS_SPLIT"
    ENUM_TX_STOCK_PLAN_POOL_ADJUSTMENT = "TX_STOCK_PLAN_POOL_ADJUSTMENT"
    ENUM_TX_STOCK_PLAN_RETURN_TO_POOL = "TX_STOCK_PLAN_RETURN_TO_POOL"
    ENUM_TX_CONVERTIBLE_ACCEPTANCE = "TX_CONVERTIBLE_ACCEPTANCE"
    ENUM_TX_CONVERTIBLE_CANCELLATION = "TX_CONVERTIBLE_CANCELLATION"
    ENUM_TX_CONVERTIBLE_CONVERSION = "TX_CONVERTIBLE_CONVERSION"
    ENUM_TX_CONVERTIBLE_ISSUANCE = "TX_CONVERTIBLE_ISSUANCE"
    ENUM_TX_CONVERTIBLE_RETRACTION = "TX_CONVERTIBLE_RETRACTION"
    ENUM_TX_CONVERTIBLE_TRANSFER = "TX_CONVERTIBLE_TRANSFER"
    ENUM_TX_EQUITY_COMPENSATION_ACCEPTANCE = "TX_EQUITY_COMPENSATION_ACCEPTANCE"
    ENUM_TX_EQUITY_COMPENSATION_CANCELLATION = "TX_EQUITY_COMPENSATION_CANCELLATION"
    ENUM_TX_EQUITY_COMPENSATION_EXERCISE = "TX_EQUITY_COMPENSATION_EXERCISE"
    ENUM_TX_EQUITY_COMPENSATION_ISSUANCE = "TX_EQUITY_COMPENSATION_ISSUANCE"
    ENUM_TX_EQUITY_COMPENSATION_RELEASE = "TX_EQUITY_COMPENSATION_RELEASE"
    ENUM_TX_EQUITY_COMPENSATION_RETRACTION = "TX_EQUITY_COMPENSATION_RETRACTION"
    ENUM_TX_EQUITY_COMPENSATION_TRANSFER = "TX_EQUITY_COMPENSATION_TRANSFER"
    ENUM_TX_PLAN_SECURITY_ACCEPTANCE = "TX_PLAN_SECURITY_ACCEPTANCE"
    ENUM_TX_PLAN_SECURITY_CANCELLATION = "TX_PLAN_SECURITY_CANCELLATION"
    ENUM_TX_PLAN_SECURITY_EXERCISE = "TX_PLAN_SECURITY_EXERCISE"
    ENUM_TX_PLAN_SECURITY_ISSUANCE = "TX_PLAN_SECURITY_ISSUANCE"
    ENUM_TX_PLAN_SECURITY_RELEASE = "TX_PLAN_SECURITY_RELEASE"
    ENUM_TX_PLAN_SECURITY_RETRACTION = "TX_PLAN_SECURITY_RETRACTION"
    ENUM_TX_PLAN_SECURITY_TRANSFER = "TX_PLAN_SECURITY_TRANSFER"
    ENUM_TX_STOCK_ACCEPTANCE = "TX_STOCK_ACCEPTANCE"
    ENUM_TX_STOCK_CANCELLATION = "TX_STOCK_CANCELLATION"
    ENUM_TX_STOCK_CONVERSION = "TX_STOCK_CONVERSION"
    ENUM_TX_STOCK_ISSUANCE = "TX_STOCK_ISSUANCE"
    ENUM_TX_STOCK_REISSUANCE = "TX_STOCK_REISSUANCE"
    ENUM_TX_STOCK_REPURCHASE = "TX_STOCK_REPURCHASE"
    ENUM_TX_STOCK_RETRACTION = "TX_STOCK_RETRACTION"
    ENUM_TX_STOCK_TRANSFER = "TX_STOCK_TRANSFER"
    ENUM_TX_WARRANT_ACCEPTANCE = "TX_WARRANT_ACCEPTANCE"
    ENUM_TX_WARRANT_CANCELLATION = "TX_WARRANT_CANCELLATION"
    ENUM_TX_WARRANT_EXERCISE = "TX_WARRANT_EXERCISE"
    ENUM_TX_WARRANT_ISSUANCE = "TX_WARRANT_ISSUANCE"
    ENUM_TX_WARRANT_RETRACTION = "TX_WARRANT_RETRACTION"
    ENUM_TX_WARRANT_TRANSFER = "TX_WARRANT_TRANSFER"
    ENUM_TX_VESTING_ACCELERATION = "TX_VESTING_ACCELERATION"
    ENUM_TX_VESTING_START = "TX_VESTING_START"
    ENUM_TX_VESTING_EVENT = "TX_VESTING_EVENT"
