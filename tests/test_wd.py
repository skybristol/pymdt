import random
import pymdt.wd


def test_build_user_agent():
    assert isinstance(pymdt.wd.build_user_agent(), str)

def test_get_wd_by_property():
    property_key_value = random.choice(list(pymdt.wd.property_mapping.keys()))

    assert isinstance(pymdt.wd.get_wd_by_property(property_key_value), list)