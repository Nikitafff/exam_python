from typing import Generator


class Pizza:
    base_ingredients: dict = {
        'dough': 100,
        'tomato paste': 50
    }

    def __attrs__(self) -> Generator:
        """Returns generator with object attributes defined by user"""
        return (attr for attr in dir(self) if not attr.startswith('_'))

    def __dict__(self):
        attrs = (getattr(self, atr) for atr in self.__attrs__())
        return {key: val for d in attrs for key, val in d.items()}

    def __str__(self):
        key_value = (f'{key} {value} г' for key, value in self.__dict__().items())
        return f'{self.__class__.__name__}: {", ".join(key_value)}'


class Margarita(Pizza):
    topping: dict = {
        'tomatoes': 50,
        'cheese': 100
    }


class Pepperoni(Pizza):
    topping: dict = {
        'pepperoni': 150,
        'cheese': 100
    }


class Hawaiian(Pizza):
    topping: dict = {
        'chicken': 150,
        'cheese': 100,
        'pineapples': 100
    }

