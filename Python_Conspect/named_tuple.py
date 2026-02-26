# namedtuple создаёт классы-рекорды (record), без методов, с одними полями
# инмыми словами: DTO. namedtuple реализует корректные дандеры для сравнения по значению,
# __repr__, __init__.

import typing
from collections import namedtuple
from dataclasses import dataclass

# 1.
Coordinate = namedtuple('Coordinate', 'lat lon')
print(issubclass(Coordinate, tuple))
# True
moscow = Coordinate(55.756, 37.617)
print(moscow)
print(moscow == Coordinate(lat=55.756, lon=37.617))
# True

# 2.
# Есть ещё typing.NamedTuple: это всё тоже самое + аннотации типов
Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
print(typing.get_type_hints(Coordinate))
# {'lat': <class 'float'>, 'lon': <class 'float'>}

# 3.
# Ещё можно наследоваться от NamedTuple


class Coordinate(typing.NamedTuple):
    lat: float  # и описываем аннотации типов тут
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'

        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


# 4.
# Ещё рекорды можно делать через декоратор @dataclass
# отличие в том, что тут используется метакласс, а не наследование, поэтому Coordinate наследууется не от NamedTuple, а от object


@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def __str__(self) -> str:
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
