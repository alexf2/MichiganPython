import decimal
import fractions
import functools
import html
import numbers
import time
from collections import abc
from functools import singledispatch

'''
Стандартные декораторы: functools.wraps,  property,	 classmethod и staticmethod.
    functools.cache - мемоизация параметров функции
    
    @functools.cache
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n - 2) + fibonacci(n - 1) 
        
    if __name__ == '__main__':
        print(fibonacci(6))
'''


def decor(func):
    def inner_function(x, y):
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        return func(x, y)
    return inner_function


@decor
def sub(a, b):
    res = a - b
    return res


print(sub(30, 20))
print(sub(10, -5))

# Пример правильного декаратора


def clock(func):
    # этот хелпер копирует __doc__ и __name__ в новую функцию и правильно разбирает аргументы
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0

        name = func.__name__
        arg_lst = [repr(arg) for arg in args]
        arg_lst.extend(f'{k}={v!r}' for k, v in kwargs.items())
        arg_str = ', '.join(arg_lst)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')

        return result
    return clocked


# Если нужен декоратор с параметрами, то нужно использовать обёртку
# ещё один уровень:
'''
def clock(fmt=DEFAULT_FMT):
    def decorate(func): 
        def clocked(*_args): 
            pass
            
        return clocked

    return decorate
'''

'''
Очень полезный декоратор singledispatch.
В Python нет перегруки сигнатур функций, как в Java. Нельзя объявить одну функцию с разными наборами и типами параметров.
Декоратор singledispatch это заменяет.
'''


@singledispatch
def htmlize(obj: object) -> str:
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


@htmlize.register
def _(text: str) -> str:
    content = html.escape(text).replace('\n', '<br/>\n')
    return f'<p>{content}</p>'


@htmlize.register
def _(seq: abc.Sequence) -> str:
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


@htmlize.register
def _(n: numbers.Integral) -> str:
    return f'<pre>{n} (0x{n:x})</pre>'


@htmlize.register
def _(n: bool) -> str:
    return f'<pre>{n}</pre>'


@htmlize.register(fractions.Fraction)
def _(x) -> str:
    frac = fractions.Fraction(x)
    return f'<pre>{frac.numerator}/{frac.denominator}</pre>'


@htmlize.register(decimal.Decimal)
@htmlize.register(float)
def _(x) -> str:
    frac = fractions.Fraction(x).limit_denominator()
    return f'<pre>{x} ({frac.numerator}/{frac.denominator})</pre>'


'''
Если	 есть	 возможность,	 регистрируйте	 специализированные	 функции	для	 обработки	 ABC	 
(абстрактных	 классов),	 например	 numbers.Integral	 или	 abc. MutableSequence,	 
а  не	 конкретных	 реализаций,	 например	 int	 или	 list.	 
Это	 позво- лит	программе	поддержать	более	широкий	спектр	совместимых	типов.	
Напри- мер,	расширение	Python	может	предоставлять	альтернативы	типу	int	с фикси- рованной	длиной	
в битах	в качестве	подклассов	numbers.Integral4.
'''

# Декоратор можно описать и классом
DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


class clock_dec:
    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            # применение переменных к шаблону
            print(self.fmt.format(**locals()))
            return _result
        return clocked
