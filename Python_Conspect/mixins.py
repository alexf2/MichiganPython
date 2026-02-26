# Миксин не имеет базового класса (он object), но вызывает super(), поэтому, если его указать первым в списке наследования,
# будет вызван метод из класса, который правее в списке на том же уровне.

import collections


def _upper(key):
    try:
        return key.upper()
    except AttributeError:
        return key


class UpperCaseMixin:
    def __setitem__(self, key, item):
        super().__setitem__(_upper(key), item)

    def __getitem__(self, key):
        return super().__getitem__(_upper(key))

    def get(self, key, default=None):
        return super().get(_upper(key), default)

    def __contains__(self, key):
        return super().__contains__(_upper(key))

# Хотя базы нет, но super() при подмешивании класса с левой стороны передаст управление одноимённому
# методу соседнего класса в списке наследования.


class UpperDict(UpperCaseMixin, collections.UserDict):
    pass
