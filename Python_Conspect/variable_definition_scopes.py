# В Питоне 4 области видимости: LEGB
# local
# enclosing (nonlocal)
# global
# built-in (и __builtins__.dict)

print(dir(__builtins__))

my_var = 10


def my_function():
    # Описываем переменную как глобальную...
    global my_var
    # Теперь глобальную переменную можно обрабатывать прямо внутри функции,
    # например - переопределить:
    my_var = 5
    print('Внутри функции:', my_var)
    # ...и снова переопределить:
    my_var += 95
    print('Внутри функции после изменений:', my_var)


my_function()
print('Снаружи функции:', my_var)


def outer_function():
    value = 10

    def inner_function():
        nonlocal value
        value = 20

    inner_function()
    print(value)


outer_function()

# Будет напечатано: 20


global_value = 10

# Словари переменных


def any_function():
    local_value = 20
    local_text = 'Локальная строка'
    global global_value
    global_value = 100500  # Изменяем глобальную переменную.
    # Печатаем словарь с объектами локального пространства функции:
    print(f'Локальные переменные в функции any_function(): {locals()}')


any_function()

# Печатаем словарь с объектами глобального пространства программы:
print(f'Глобальные переменные программы: {globals()}')
