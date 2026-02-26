import time
from functools import lru_cache


def sleep_one_sec():
    print('Функция sleep_one_sec() начала вычисления.')
    print('Вычисляю...')
    time.sleep(1)
    return 'Функция sleep_one_sec() завершила вычисления.'


def time_of_function(func):
    def wrapper():
        start_time = time.time()
        print('Время пошло')
        result = func()
        execution_time = round(time.time() - start_time, 3)
        print(f'Через {execution_time} сек. функция вернула «{result}»')
        return result
    return wrapper


result = time_of_function(sleep_one_sec)()
print(result)


def time_of_function2(func):
    def wrapper():
        start_time = time.time()
        result = func()
        execution_time = round(time.time() - start_time, 3)
        print(f'Время выполнения: {execution_time} сек.')
        return result
    return wrapper


@time_of_function2
@lru_cache
def expensive_computation():
    sequence = [1]
    for item in range(10000):
        sequence.append(sum(sequence))
    return sequence[10]


print(expensive_computation())

print(expensive_computation())

print(expensive_computation())
