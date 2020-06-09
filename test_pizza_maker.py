import pizza_maker
import re
import pytest


def test_class_attributes():
    """Checking for Non empty attributes"""
    for _class in pizza_maker.Pizza.__subclasses__():
        for attr in _class.__attrs__(_class):

            assert attr, 'Ingredients attribute is empty'


def test_str():
    """Checking that tomato paste is in string"""
    for _class in pizza_maker.Pizza.__subclasses__():
        pizza = _class()

        assert re.search('tomato paste', str(pizza)), 'Tomato paste is a must'


def test_dict():
    """Checking new __dict__ method + all ingredients must by int"""
    for _class in pizza_maker.Pizza.__subclasses__():
        pizza = _class()
        for key, value in pizza.__dict__().items():

            assert isinstance(value, int), 'All ingredients must by int'


@pytest.mark.parametrize('s, exp', [
    ('base_ingredients', 2),
    ('topping', 1)
])
def test_ingredients_count(s, exp):
    """Pizza should have a least 2 base and 1 topping"""
    for _class in pizza_maker.Pizza.__subclasses__():
        pizza = _class()
        assert len(getattr(pizza, s)) >= exp
