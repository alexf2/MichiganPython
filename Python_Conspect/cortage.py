digits = (1, 2, 3, 4, 5)
fruits = ('яблоко', 'банан', 'вишня')
nn = 1, 2, 3
print(type(fruits))
print(type(nn))

letters = tuple('яблоко')  
print(type(letters), letters)

# Передаём список в функцию tuple():
apples = tuple(['Голден', 'Карамелька', 'Антоновка'])
print(type(apples), apples)

fruits = 'яблоко', 'банан', 'вишня'
print(type(fruits))
print(fruits)

'''
Особенности кортежей
Неизменяемость. После объявления кортежа в него нельзя добавить элементы, удалить или заменить их. Это свойство выглядит как недостаток, однако за счёт этой особенности кортеж получает заметные преимущества.
Меньший объём в памяти: при прочих равных кортежи занимают меньший объём в памяти, чем списки.
'''

def reversed_sort(data):
    return tuple(sorted(data, reverse=True))


def bizarre_function(first, second, third):
    total = first + second + third
    multiplication = first * second * third
    string = str(first) + str(second) + str(third)
    # Перечисление значений через запятую - это способ объявить кортеж!
    return total, multiplication, string

# packing
a=10
b=20
c=30
d=40
t=a, b, c, d
print(t)

#unpacking
t=(10, 20, 30, 40)
a, b, c, d = t