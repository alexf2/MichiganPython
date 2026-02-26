# match /case поддерживает именованные и позиционные образцы

class Vector2d:
    __match_args__ = ('x', 'y')  # это для поддержки позиционного match / case
    # тут мы указываем в каком порядке сопоставляются поля

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

# именованные образцы


def keyword_pattern_demo(v: Vector2d) -> None:
    match v:
        case Vector2d(x=0, y=0):
            print(f'{v!r} is null')
        case Vector2d(x=0):
            print(f'{v!r} is vertical')
        case Vector2d(y=0):
            print(f'{v!r} is horizontal')
        case Vector2d(x=x, y=y) if x == y:
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is awesome')


# позиционные образцы
def positional_pattern_demo(v: Vector2d) -> None:
    match v:
        case Vector2d(0, 0):
            print(f'{v!r} is null')
        case Vector2d(0):
            print(f'{v!r} is vertical')
        case Vector2d(_, 0):
            print(f'{v!r} is horizontal')
        case Vector2d(x, y) if x == y:
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is awesome')


vv = (Vector2d(2, 4), Vector2d(4, 4), Vector2d(
    0, 1), Vector2d(1, 0), Vector2d(4, 4))

for v in vv:
    keyword_pattern_demo(v)
    positional_pattern_demo(v)
