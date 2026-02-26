# !!! https://www.geeksforgeeks.org/python-programming-language - хороший учебник по Питону
# DOC: https://docs.python.org/3.12/
# Tutorial: https://www.geeksforgeeks.org/python3-tutorial/
# Tutorial MS: https://dotnettutorials.net/lesson/introduction-to-python/
#
# Built in functions: https://docs.python.org/3.9/library/functions.html
#
# Std modules: https://docs.python.org/3/library/index.html
# ---------------------------------------------------------------------------------------

# Python 3  built-in data types: integers, floats, strings, booleans, lists, tuples, and dictionaries.

# В языке Python — сильная типизация.
'''
Python — язык с динамической и сильной типизацией:
    одна переменная может принять значения разных типов,
    Python сам не приводит данные к нужному типу.
    в Python нельзя выполнять операции с несовместимыми типами.
    Python позволяет перевести значение переменной из одного типа в другой — для этого используются специальные функции.
'''

'''
    Numeric types (int, Float, Complex)
    bool
    None
    Str
    Bytes
    Bytearray
    Tuple
    List
    Range
    Set
    dict
    
The bytearray data type is the same as the bytes data type, but bytearray is mutable means we can modify the content of bytearray data type. 
'''

x = [10, 20, 100, 40, 15]
y = bytes(x)
print(type(y))

# arithmetic operators (+, -, *, /, %, **, //), comparison operators (>, <, ==, !=), and logical operators (and, or, not)
# membership operators: in, not in, identity operators: is, is not, id.
# привсоение: =, +=, -=


# Операции: https://dotnettutorials.net/lesson/operators-in-python/

a = 20
b = 12
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

print('------------')

a = 13
b = 5
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

print('------------')

x = 5
y = 0
print(not x)
print(not y)

print('------------')

names = ["Ramesh", "Nireekshan", "Arjun", "Prasad"]
print("Nireekshan" in names)
print("Hari" in names)
print("Hema" not in names)

print('------------')

# identity - адрес
a = 26
b = 25
print(id(a))
print(id(b))
c = [1, 2, 3]
k = c
print(id(c))
print(id(k))

print('------------')

a = 25
b = 25
print(a is b)
print(id(a))
print(id(b))

print('------------')

a = 25
b = 30
print(a is b)
print(id(a))
print(id(b))

