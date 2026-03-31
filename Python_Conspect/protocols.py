from typing import Protocol

'''
Протоколы в Python — это неформальные интерфейсы, определяющие набор методов, которые класс должен реализовать 
для определённого поведения. Это основа утиной типизации.

Преимущества:
  Полиморфизм без наследования — разные классы работают с одним API.
  Структурная типизация — проверка по поведению, не по имени класса.
'''


class MyList:
    def __len__(self):      # Протокол Sized
        return 42

    def __getitem__(self, i):  # Протокол Sequence
        return i * 2

    def __iter__(self):     # Протокол Iterable
        return iter([1, 2, 3])


lst = MyList()
print(len(lst))         # 42 ✓
print(lst[0])           # 0 ✓
for x in lst:
    print(x)  # Работает! ✓


class Drawable(Protocol):
    def draw(self) -> None:
        ...


class Circle:
    def draw(self) -> None:
        print("Circle")  # Реализуем протокол


def render(shape: Drawable):
    shape.draw()


render(Circle())  # OK для mypy

'''
Протокол	Методы	    Пример использования
Sized	    __len__	    len(obj)
Iterable	__iter__	  for x in obj
ContextManager	__enter__, __exit__	with obj:
Callable	  __call__	obj()
'''
