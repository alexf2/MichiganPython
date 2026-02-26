# Конкатенация последовательностей

first_vegetable_list = ['помидор', 'огурец', 'баклажан', 'перец']

second_vegetable_list= ['картофель', 'морковь', 'лук', 'чеснок']

full_vegetable_list = first_vegetable_list + second_vegetable_list
print(full_vegetable_list)

# Строки - это последовательности. Объединяем!
hybrid = second_vegetable_list[3] + first_vegetable_list[1]
print(hybrid)


# Умножение
dig_more = 'копаю грядку! ' * 4
print(dig_more)

small_vegetable_list = ['Редиска', 'Картошка', 'Морковка']
double_vegetable_list = small_vegetable_list * 2
print(double_vegetable_list)

# Слайсы
vegetable_name = 'Ананас'
print(vegetable_name[1:5])