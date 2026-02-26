# new_sequence = [<значение_элемента> for <переменная_цикла> in <исходный_список>]
#
# Компрехенжены бываю списковые [...] и генераторные (...).
# Вторые не материализуются сразу, а работают как yield.

import random
from statistics import mean
# Сперва выполним эту задачу в обычном цикле
from typing import List

new_sequence: List[int] = []

for value in range(6):
    list.append(new_sequence, value * 3)

print(new_sequence)

# А теперь то же самое запишем в сокращённой форме:
new_sequence_better = [value * 3 for value in range(6)]  # Всё!
print(new_sequence_better)


vegetables = ['Помидор', 'Огурец', 'Капуста']
category = 'Овощная культура'

vegetables_info = {vegetable: category for vegetable in vegetables}
#       Создаём     ключ    и  значение.

print(vegetables_info)


# Условия в компрехенжинах

fruit_yields = [164.8, 105.0, 124.3, 113.8]
# Присвоить новому элементу значение yield_value, ЕСЛИ yield_value > 120.
new_yields = [yield_value for yield_value in fruit_yields if yield_value > 120]

print(new_yields)


# any и all

vegetable_yields = [6.5, 4.3, 2.8, -3.8, 2.2, 3.5]

# Все ли проверки вернули True?
are_all_positive = all(
    [vegetable_yield > 0 for vegetable_yield in vegetable_yields])

# Есть ли хоть один элемент, вернувший True?
are_any_positive = any(
    [vegetable_yield > 0 for vegetable_yield in vegetable_yields])

print('Все ли элементы вернули True?', are_all_positive)
print('Есть ли хоть один элемент, вернувший True?', are_any_positive)


# Матрица
rows = 3
cols = 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print(matrix)


# Подсчёт суммы и среднего в матрице

# Пригодится для наполнения списков!

# 1. Создание списка списков:
# Примените list comprehension.
harvest = [[random.randint(5, 20) for _ in range(5)] for _ in range(5)]

# 2. Функция для подсчёта общего урожая:


def total_harvest(h):
    summ = 0
    for row in h:
        summ += sum(row)
    return summ

# 3. Функция для подсчёта среднего урожая с каждого участка:


def average_harvest_per_plot(h):
    return [mean(item) for item in h]


# Вывод результатов
print('Урожай с каждой грядки на каждом участке:', harvest)
print('Общий урожай со всех участков:', total_harvest(harvest))
print('Средний урожай с каждого участка:', average_harvest_per_plot(harvest))


# Декартово произведение
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
