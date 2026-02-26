# from functools import reduce

# Генератор хранит в памяти не элементы, а внутреннее состояние для вычисления очередного элемента. 
# На каждом шаге можно вычислить только следующий элемент, но не предыдущий.
# Генератор, исчерпавший все свои значения, помнит своё состояние («я всё сделал!»), 
# поэтому повторное обращение к нему не вернёт никакого результата. Второй раз подряд проитерироваться по генератору 
# не получится.


def m():
    yield 'Mahesh'
    yield 'Suresh'


g = m()

print(g)
print(type(g))

for y in g:
    print(y)


def fibo(n):
    if not isinstance(n, int) or n < 1:
        yield None
        return

    if n == 1:
        yield 0
        return

    yield 0
    yield 1
    n -= 2
    prev = 0
    current = 1
    while n > 0:
        [prev, current] = [current, prev + current]
        n -= 1
        yield current


for i in range(0, 16):
    res = []
    for f in fibo(i):
        res.append(f)
    print(i, ':---', res)


def m2():
    yield 'Mahesh'
    yield 'Suresh'


g = m2()
print(type(g))
print(next(g))
print(next(g))

print(__name__)
print(__package__)

# -------------------------


def short_sequence():
    num = 1
    while num < 5:
        # Сгенерировать значение через yield.
        yield num
        num += 1


# Здесь функция-генератор возвращает итератор.
step = short_sequence()

# Обратиться к методу __next__() итератора
# и получить первое значение последовательности.
print(step.__next__())

# ---------------------

# Так описыается список через list comprehension.
simple_list = [digit for digit in range(2)]

print(type(simple_list))
a = iter(simple_list)
print(a.__next__())
print(a.__next__())

# Выведется:
# <class 'list'>
# 0
# 1

# А так описывается генераторное выражение.
simple_generator = (digit for digit in range(2))

print(type(simple_generator))
print(simple_generator.__next__())
print(simple_generator.__next__())

# Выведется:
# <class 'generator'>
# 0
# 1


# -----------------------


# Список для тестирования.
numbers = [1, 3, 4, 6, 9, 11]

# Здесь напишите ваше генераторное выражение.
digits = (digit ** 2 for digit in numbers if digit % 3 == 0)

# Распечатайте сумму квадратов.
# summ = reduce(lambda prev, el: prev + el ** 2, digits, 0)
summ2 = sum(digits)
print(summ2)
