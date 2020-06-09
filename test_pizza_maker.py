import pizza_maker
import re
import pytest


def test_class_attributes():
    for _class in pizza_maker.Pizza.__subclasses__():
        for attr in _class.__attrs__(_class):

            assert attr, 'Ingredients attribute is empty'


def test_str():
    for _class in pizza_maker.Pizza.__subclasses__():
        pizza = _class()

        assert re.search('tomato paste', str(pizza)), 'Tomato paste is a must'


def test_dict():
    for _class in pizza_maker.Pizza.__subclasses__():
        pizza = _class()
        for key, value in pizza.__dict__().items():

            assert isinstance(value, int), 'All ingredients must by int'

