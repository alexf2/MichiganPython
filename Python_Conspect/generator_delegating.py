def gen():
    yield 1
    # здесь делегация генератору
    # вместо цикла:
    #   for i in sub_gen():
    #     yield i
    yield from sub_gen()
    yield 2


def sub_gen():
    yield 1.1
    yield 1.2


for i in gen():
    print(i)
