'''
    All functions in Python are first-class functions. 
    To say that functions are first-class in a certain programming language means that they can be passed around 
    and manipulated in the same way as to how you would pass around and manipulate other kinds of objects (like integers or strings). 
    You can assign a function to a variable
'''

'''
Модификаторы переменных:
    nonlocal - переменная выше уровнем внутри замыкания;
    global - глобальная переменная.
    
    В Питоне 3 области видимости: local, nonlocal (свободная переменная) и global.
    
    - если	x –	параметр	или	ей	присвоено	значение	в теле	функции,	то	x –	 л о - кальная	переменная;
    - если	 на	 x  имеется	 ссылка,	 но	 значение	 ей	 не  присвоено	 и  параметром	она	тоже	не является,	то:
        - x	 ищется	 в  локальных	 областях	 видимости	 тел	 объемлющих	 функ- ций	(нелокальных	областях	видимости);
        - если	она	не найдена	в объемлющих	областях	видимости,	то	читает- ся	из	глобальной	области	видимости	модуля;
        - если	она	не найдена		и в	глобальной	области	видимости,	то	читается	из	__builtins__.__dict__
'''
# пример с глобальной переменной b: строчка b = 9 приведёт к ошибке в строчке print(b), если не добавить global.
# Защищает от случайной модификации другой переменной. Лучьше, чем в JS.
b = 6


def f2(a):
    global b

    print(a)
    print(b)
    b = 9


f2(3)


def summ(arg=None):
    s = 0 if arg is None else arg

    def inner(a=None):
        nonlocal s
        if a is None:
            return s
        else:
            s += a
            return inner

    return s if arg is None else inner


print(summ())
print(summ(2)(1)())
print(summ(5)())
print(summ(7)(3)(2)())

'''
    Типы аргументов:
    
    Positional arguments
    Keyword arguments
    Default arguments
    Variable-length arguments
    keyword variable-length argument
'''

# Пример с вариадичскими параметрами:
# / - отделяет обязательные позиционные параметры
# * - это позиционные параметры переменной длины, соберутся в кортеж
# class_ - это имнованный параметр, который можно передавать только по имени
# **attrs - это словарь именованных параметров (должны передаваться с именем)
# * - делает параметр сборщиком значений в кортеж, а ** - делает параметр
# сборщиком пар имя=значение в словарь.


def tag(name, /, *content, class_=None, **attrs):
    pass

# Variable-length argument


def total_cost(x, *y):
    sum = 0
    for i in y:
        sum += i
    print(x + sum)


# calling function
total_cost(100, 200)  # valid
total_cost(110, 226, 311)  # valid
total_cost(11,)  # valid

# keyword variable length argument


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(id=1, name="Nireekshan", qualification="MCA")


def m1(**x):
    for k, v in x.items():
        print(k, "=", v)


m1(a=10, b=20, c=30)
m1(id=100, name="Subbalaxmi")


# global and local variables having the same name
a = 1


def m1():
    global a
    a = 2
    print("a value from m1() function: ", a)


def m2():
    print("a value from m2() function:", a)


m1()
m2()

# доступ к глобальной переменной
a = 1


def m():
    a = 2
    print(a)
    print(globals()["a"])


m()
