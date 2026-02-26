import bisect
import random

SIZE = 7

random.seed(1729)

my_list = [-1, 1, 5, 10, 15, 20, 30, 40, 50]
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    # Вставляет элемент в уже отсортированный list в правильную точку
    bisect.insort(my_list, new_item)
    print(new_item)


print(my_list)
