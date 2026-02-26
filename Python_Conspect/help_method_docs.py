# Чтобы получить справку по методам, на примере list:

print(dir(list))
print(help(list.append))

# А так можно получить тип объекта и создать новый инстанс:
tt = type([])
lst = tt((1, 2, 3))
print(lst)
