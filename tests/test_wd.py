import random
from pymdt.wd import build_user_agent, get_wd_by_property, property_mapping


def test_build_user_agent():
    assert isinstance(build_user_agent(), str)


def test_get_wd_by_property():
    property_key_value = random.choice(list(property_mapping.keys()))

    assert isinstance(get_wd_by_property(property_key_value), list)
