from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


NOT_SPECIFIED = object()


def self_getter(val):
    return val


def max(*args, val_getter=None, default=NOT_SPECIFIED):
    it = iter(args)
    try:
        next(it)
    except StopIteration:
        if default is NOT_SPECIFIED:
            raise ValueError('max() args is an empty sequence.')
        return default

    getter = val_getter if val_getter else self_getter

    val = None
    for v in args:
        curr_val = getter(v)
        if hasattr(curr_val, '__iter__'):
            curr_val = max(*curr_val, val_getter=val_getter, default=default)
        if val is None or val < curr_val:
            val = curr_val

    return val


test_users = (User(name='Ivan', age=32), User(name='Alex', age=42), User(name='Anna', age=29))


def test():
    print(max(1))
    print(max(-1, 2, 1))
    print(max(0, -1))
    print(max(-2, 0))
    print(max(2, 11, 0, -2, 12, 7, 2, 4, 7, 22, 21))
    print(max(*test_users, val_getter=lambda u: u.age))

    try:
        max()
    except Exception as ex:
        print(repr(ex))

    try:
        max(*[])
    except Exception as ex:
        print(repr(ex))

    print(max(*[], default=0))

    print(max([7, 2, 1, 0]))
    print(max([], default=-1))


if __name__ == "__main__":
    test()
