import itertools
import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    # идеоматическая реализация итератора на Python
    def __iter__(self):
        for word in self.words:
            yield word
        # ещё можно так:
        # return iter(self.words)
        # или
        # yield from self.words


class SentenceLeazy:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        # finditer возвращает генератор
        for match in RE_WORD.finditer(self.text):
            yield match.group()

        # ещё вариант:
        # return (match.group() for match in RE_WORD.finditer(self.text))


class ArithmeticProgression:
    """Итератор арифметической прогрессии."""

    def __init__(self, begin, step, end=None):
        """Инициализация прогрессии.

        Args:
            begin: Начальное значение.
            step: Шаг прогрессии.
            end: Конечное значение (не включительно). 
                 Если None, генерирует бесконечно.
        """
        self.begin = begin
        self.step = step
        self.end = end  # None -> "бесконечный" ряд

    def __iter__(self):
        """Возвращает итератор прогрессии."""
        result_type = type(self.begin + self.step)
        result = result_type(self.begin)
        forever = self.end is None
        index = 0

        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


# ещё короче, правда, при дробном шаге прогрессия менее точная, так как
# в предыдущим варианте у нах умножение self.step * index, а тут прибавление шага
# а float не точный тип, и накапливается погрешность
def aritprog_gen(begin, step, end=None):
    """Генератор арифметической прогрессии.

    Args:
        begin: Начальное значение прогрессии.
        step: Шаг прогрессии.
        end: Конечное значение (не включительно). Если None, генерирует бесконечно.

    Yields:
        Последовательность чисел арифметической прогрессии.
    """
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)

    if end is None:
        return ap_gen

    return itertools.takewhile(lambda n: n < end, ap_gen)


""" 
Генераторные функции в itertools:
    - Фильтрующие генераторные функции: filter, takewhile;
    - Отображающие генераторные функции: enumerate;
    - Генераторные функции, объединяющие несколько входных итерируемых объектов: chain, product, zip
    - Генераторные функции, расширяющие каждый входной элемент в несколько выходных: count, permutations, repeat, pairwise;
    - Реорганизующие генераторные функции: groupby, reversed;
    - Редуцирование: Встроенные функции, которые читают итерируемый объект и возвращают одиночное значение: any, all, reduce, sum.
"""
