# Задание для экзамена 
## Classes

- описать классами рецепты 3-х пицц
- общие ингредиенты: тесто, томатная паста
- метод `dict(self)` возвращает словарь рецепта, 
  например: `Foo.dict() == {'dough': 100, 'tomato paste': 50, ...}`
- вызов `str(Foo())` возвращает рецепт строкой, 
  например: `str(Foo()) == 'Пеперони: dough 100г, tomato paste 50г, ...'`
  
  
  Тесты: `pytest pizza_maker.py`
 
  
  