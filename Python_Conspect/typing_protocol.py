# Тип Protocol это аналог интерефейса, только проверка типов происходит в рантайме. Или, как PropTypes в React.
#

from typing import Iterable, Protocol, TypeVar


# тут мы не можем правильно протипизировать элемент коллекции, поэтому берём any
def top(coll: Iterable[any], length: int) -> list[any]:
    ordered = sorted(coll, reverse=True)
    return ordered[:length]


str = 'В Python	 определение	 протокола	 записывается	 в  виде	 подкласса typing.'

words = [w.strip() for w in str.split(' ')]

print('1:', words)

ww = ((len(w), w) for w in words)
ww_lst = list(ww)
print('2:', ww_lst)
print('2.2:', list(ww))  # тут генератор уже завершился, он одноразовый

print('3:', top(words, 3))
print('3:', top(ww_lst, 3))

# теперь используем статический протокол: нам нужно, чтобы элемент коллекции
# поддерживал оператор '<', то есть, дандер __lt__


class SupportsComparision(Protocol):
    def __lt__(self, other: any) -> bool:
        pass


LT = TypeVar('LT', bound=SupportsComparision)

# теперь типизируем дженерик через протокол (аналог интерфейса)


def top2(coll: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(coll, reverse=True)
    return ordered[:length]


print('4:', top2(ww_lst, 3))

'''
так можно получить в консоль тип на основе тайпингов, который выводит Mypy:

if TYPE_CHECKING:
    reveal_type(series)
    reveal_type(expected)
    reveal_type(result)
'''
