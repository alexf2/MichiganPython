# Использование super()
class LastUpdatedOrderedDict(OrderedDict):
    """Этот код работает в Python 2 и в Python 3"""


def __setitem__(self, key, value):
    super(LastUpdatedOrderedDict, self).__setitem__(key, value)
    self.move_to_end(key)

# Теперь	оба	аргумента	super	факультативны.	Компилятор	байт-кода	в Python 3
# автоматически	подставляет	их,	исследуя	объемлющий	контекст	вызова	super() в методе.

# Наследование от: list, dict, str и других встроенных типов
# Тут не работает раннее связывание методов, поэтому они как бы невиртуальные и перегрузить нельзя.
# Для словарей надо наследоваться от UserDict, а не от dict. В нём нет этой проблемы.

# Множественное наследование: обход дерева для одинакового метода


class Root:
    def ping(self):
        print(f'{self}.ping() in Root')

    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'


class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()


class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')  # Было vprint -> исправлено на print


class Leaf(A, B):
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()


ll = Leaf()

ll.ping()
print('-' * 10)
ll.pong()

'''
<instance of Leaf>.ping() in Leaf
<instance of Leaf>.ping() in A
<instance of Leaf>.ping() in B
<instance of Leaf>.ping() in Root
----------
<instance of Leaf>.pong() in A
<instance of Leaf>.pong() in B
'''

# Для анализа связей наследования можно использовать сканирование MRO method resolution order:


def print_mro(cls):
    print(','.join(c.__name__ for c in cls.__mro__))
