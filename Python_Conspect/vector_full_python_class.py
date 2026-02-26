# Полнофункциональный класс с форматированием, итерацией, хешированием, поддержкой образцов match/case,
# сериализацией в bytes и обратно, немутабельный

import math
from array import array


class Vector2d:
    # это для экономии памяти, чтобы избавиться от __dict__
    __slots__ = ('__x', '__y')
    __match_args__ = ('x', 'y')  # это для match/case
    # это классовое свойство, оно задаёт значение по-умолчанию для класса, но в коде лучше читать как self.typecode:
    # если так делать, то при модификации self.typecode у инстанса будет уже своё, другое значение.
    typecode = 'd'  # это тип float, используется для array

    def __init__(self, x, y):
        self.__x = float(x)  # float - для защиты координат по типу
        # декорирование имен x и y (name mangling) - это для сокрытия от конфликтов
        self.__y = float(y)
        # если при наследовании объявят такое же поле. В __dict__ добавится имя _Vector2d__x.

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash((self.x, self.y))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __add__(self, v2):
        return Vector2d(self.x + v2.x, self.y + v2.y)

    def __mul__(self, m):
        return Vector2d(self.x * m, self.y * m)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    # альтернативный конструктор: для десериализации из байтов
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


vv = (Vector2d(2, 4), Vector2d(4, 4), Vector2d(
    0, 1), Vector2d(1, 0), Vector2d(4, 4))

print('test')

# распаковка в кортеж
v1, v2, v3, *rest = vv

# использование хеша
set = {v1, v2, v3}
print(set)

# проверка на нулевую длину
print(bool(v1), bool(v2), bool(Vector2d(0, 0)))

# сериализация
print(bytes(v2))

# сравнение по значению
print(Vector2d(2, 1) == Vector2d(2, 1))

# форматирование str и repr
print('str:', v2)
print('repr:', repr(v2))
print('repr:', f'{v2!r}')

# форматирование с указанием шаблона для координат
print('кастомный шаблон:', f'{v2:0.4f}')
print('кастомный шаблон, полярные координаты:', f'{v2:0.4p}')

'''
Правила для __slots__:

1. Не	забывайте	заново	объявлять __slots__	в каждом подклассе,	потому	что	унаследованный	атрибут	интерпретатор игнорирует.

2. Экземпляры	 класса	 могут	 иметь	 только	 атрибуты,	 явно	 перечисленные	в __slots__,	
если	в него	не включено	также	имя	'__dict__' (однако	при	этом	вся	экономия	памяти	может	быть	сведена	на	нет).

3. Для	 классов,	 где	 используется	 __slots__,	 нельзя	 употреблять	 декоратор	@cached_property,	если	
только	в __slots__		явно	не включено	имя	'__dict__'.

4. Экземпляры	   класса	   не    могут	   быть	   объектами	   слабых	   ссылок,	   если	не включить	в __slots__	имя	'__weakref__'.
'''
