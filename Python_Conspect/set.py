# Симметрическую разность можно найти и с помощью функции 
stepan_vegetables = {'томат', 'огурец', 'баклажан', 'лук'}
tonya_vegetables = {'огурец', 'кабачок', 'баклажан', 'морковь'}

# Создаём множество, состоящее из элементов обоих множеств, 
# с исключением пересекающихся:
sym_diff_vegetables = set.symmetric_difference(stepan_vegetables, tonya_vegetables)
print(sym_diff_vegetables)

# или

sym_diff_vegetables = stepan_vegetables ^ tonya_vegetables
print(sym_diff_vegetables)

# Разность можно найти и функцией set.difference(<set_1>, <set_2>)

# union

stepan_vegetables = {'томат', 'огурец', 'баклажан', 'лук'}
tonya_vegetables = {'огурец', 'кабачок', 'баклажан', 'морковь'}

# Создаём множество, элементы которого есть в первом ИЛИ (|) во втором множестве:
all_vegetables = set.union(stepan_vegetables, tonya_vegetables)
print(all_vegetables)


# intersection

stepan_vegetables = {'томат', 'огурец', 'баклажан', 'лук'}
tonya_vegetables = {'огурец', 'кабачок', 'баклажан', 'морковь'}

common_vegetables = set.intersection(stepan_vegetables, tonya_vegetables)
print(common_vegetables)
# Вывод в терминал: {'баклажан', 'огурец'} 