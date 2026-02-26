# С Python 3.6 ключи в dict сохраняют порядок вставки, как и в OrderedDict
# С 2.7 добавлены словарные и множественные компрехенжены.

import sys
import re
import abc
from collections import defaultdict
from dataclasses import dataclass
import builtins
from collections import ChainMap

# Разновидности словаря
# dict - приоритет на эффективность поиска и модификации, но не порядок, хотя в Python 3.6 порядок вставки сохраняется.
# OrderedDict - на первом месте эффективность упорядочивания, а итерирование и обновление - вторичны.
# подходит для LRU-cache - отслеживание последних операций доступа.
# ChainMap - объединяет несколько dict и ищет по порядку по всех.
pylookup = ChainMap(locals(), globals(), vars(builtins))
# Counter - словарь-мультимножество: он упаковывает в value счётчик одинаковых значений ключа.
# Shelf - это словарь-хранилище сериализованных через pickle объектовю
# set и frozenset - хешируемое.

# словарь можно создать по-разному
d2 = {'a': 2, 'b': 4, 'c': 6}
d2 = dict(a=2, b=4, c=6)

# Интерфесы словарей и множеств определены как абстрактные классы Mapping и MutableMapping
# в collections.abc. Их так же можно использовать при проверке.
# Иерархия наследования такая: Collection <-- Mapping <-- MutableMapping
my_dict = {}
isinstance(my_dict, abc.Mapping)

# Для реализации кастомных словарей наследуются от UserDict или используют композицию.

# Чтобы быть ключом словаря, объект должен иметь __hash__() и __eq__(), и у равных объектов равны и хэши.
# Все немутабельные типы хешируемы, а tuple хешируем, если хешируемы его элементы.

# Добавление элемента в словарь с дефолтным значением (удобно для массивов, объектов)
WORD_RE = re.compile(r'\w+')
index = {}

with open(sys.argv[1], encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # !!! тут используем не get и set, а setdefault
            # он нам даст либо существующий массив из словаря, либо новый пустой
            index.setdefault(word, []).append(location)

# это даёт:
# if key not in my_dict:
#    my_dict[key] = []
#    my_dict[key].append(new_value)

# Ещё можно сделать, чтобы если ключа нет, то возвращался дефолт
# используя defaultdict или __missing__


@dataclass
class Counter:
    count: int = 0


acc = defaultdict(Counter)  # создаём инстанс словаря с фабрикой для дефолта
acc[key].count += 1  # а тут инкрементируем счёткик в словаре одной строчкой

'''
Например, пусть defaultdict создан как dd = defaultdict(list). Тогда, если ключ 'new-key' отсутствует в dd, то при 
вычислении выражения dd['new-key'] выполняются следующие действия:

1. Вызвать list() для создания нового списка.
2. Вставить этот список в dd в качестве значения ключа 'new-key'.
3. Вернуть ссылку на этот список.

Вызываемый объект, порождающий значения по умолчанию, хранится в атрибуте экземпляра default_factory.
'''

# Словарный компрехенжн
dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

dic = {country: code for code, country in dial_codes}
print(dic)

# Слить два словаря распаковкой **
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}

print({**d1, **d2})

# Слить через оператор | или |=
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}

d3 = d1 | d2

print(d3)

d5 = {'mm': 12}
d5 |= d2
print(d5)

# Словарь можно передать как именованные аргументы функции, но одинаковых ключей быть не должно


def dump(**kwargs):
    print(kwargs)


d1 = {'a': 0, 'x': 4, 'y': 2, 'z': 3}
d2 = {'k': 12, 'x1': 6, 'y1': 22, 'z1': 8}

dump(**d1, m=-1, **d2)


# Сделать dic из 2-х коллекций

vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
vegetable_yields = [6.5, 4.3, 2.8, 2.2, 3.5]

# Шаг первый:
# упаковываем списки в zip:
vegetables_zip = zip(vegetables, vegetable_yields)

# Шаг второй:
# преобразуем zip в словарь:
vegetables_info = dict(vegetables_zip)

# Печатаем словарь:
print(dict(vegetables_info))


# Создать dic из нескольких списков
vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
varieties = ['Красный куб', 'Аллигатор',
             'Василёк', 'Тропический закат', 'Арктик']
yields = [6.5, 4.3, 2.8, 2.2, 3.5]


def create_vegetable_info(v, va, y):
    # Ваш код здесь
    return dict(zip(v, zip(va, y)))


create_vegetable_info(vegetables, varieties, yields)

# Словари работают в match/case, так удобно процессить JSON


def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record! r}')
