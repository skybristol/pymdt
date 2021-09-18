import pytest
from pymdt import wd
import random


def test_build_user_agent():
    assert isinstance(wd.build_user_agent(), str)

def test_get_wd_by_property():
    property_key_value = random.choice(list(wd.property_mapping.keys()))

    assert isinstance(wd.get_wd_by_property(property_key_value), list)