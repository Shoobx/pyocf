"""OCF Utils"""
import importlib
from pyocf import registry


def get_factory(ocf_type):
    module, classname = registry.OCF_TYPE_MAP[ocf_type]
    return getattr(importlib.import_module(module), classname)
