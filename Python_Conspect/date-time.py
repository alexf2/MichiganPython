ff = [1, 2, 3, 4, 5, 6]

*name, amt, dt = ff

print(amt, dt)
print(name)

# Formatting

from datetime import datetime

deadline = datetime(2023, 11, 6, 13, 0, 0)
# Синтаксис: datetime.strftime(<дата>, 'шаблон_для_форматирования')
deadline_as_str = datetime.strftime(deadline, '%Y/%m/%d %H:%M')
print('Ваш дедлайн:', deadline_as_str)


# Парсинг

from datetime import datetime

datetime_str = '09/19/22 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
print(f'strptime: {datetime_object}')



# Time

# Из модуля datetime импортирован нужный тип данных - на этот раз time.
from datetime import time

# Переменной meeting_time присвоено значение типа time.
# Нулевые значения можно записывать одним или двумя нулями;
# значения в диапазоне от 1 до 9 необходимо записывать 
# одним символом, без 0: 9, а не 09.
meeting_time = time(9, 15, 00)

print('Презентация проекта состоится в', meeting_time)
print(type(meeting_time))



# Current date and time

from datetime import datetime, date

# При помощи now() получаем текущую дату и время.
now = datetime.now()  
# При помощи today() получаем текущую дату.
today_1 = datetime.today()
today_2 = date.today()

print('Сегодняшняя дата и текущее время через now():', now, type(now))
print('Сегодняшняя дата через datetime и today():', today_1, type(today_1))
print('Сегодняшняя дата через date и today():', today_2, type(today_2))



# Replacing

from datetime import datetime

datetime1 = datetime(2023, 8, 13, 3, 0, 0)  # 13 августа 2023 года, 3 утра
datetime2 = datetime.replace(datetime1, year=2019)  # 13 августа 2019 года, 3 утра

print('Исходная дата:', datetime1)
print('Изменённая дата:', datetime2)



# Comparing

from datetime import datetime

deadline = datetime(2023, 11, 6, 13, 00, 00)
today = datetime(2023, 10, 12)

print(deadline > today)


# Delta

from datetime import datetime, timedelta

deadline_detail = datetime(2023, 11, 6, 13, 00, 00)
today_detail = datetime(2023, 10, 12, 22, 13, 55)

print(timedelta.total_seconds(deadline_detail - today_detail))



from datetime import datetime, date

deadline = date(2023, 11, 6)
today = date(2023, 10, 12)

deadline_detail = datetime(2023, 11, 6, 9, 15, 00)
today_detail = datetime(2023, 10, 12, 22, 13, 55)

print('Разность дат:', deadline - today, type(deadline - today))
print('Разность дат и времени:', deadline_detail - today_detail, type(deadline_detail - today_detail))


# Преобразования

from datetime import datetime

exact_deadline = datetime(2023, 11, 6, 9, 15, 00)

# Из типа datetime получен тип date.
date_from_datetime = datetime.date(exact_deadline)
print('Ваш дедлайн:', date_from_datetime)

# Из типа datetime получен тип time.
time_from_datetime = datetime.time(exact_deadline)
print('Презентация проекта состоится в', time_from_datetime)


# Получить дни

# Допишите нужные импорты.
from datetime import datetime, timedelta

MASK = '%Y/%m/%d %H:%M:%S'

def timedelta_days(datetime_str_1, datetime_str_2):
    # Напишите тело функции.
    return (datetime.strptime(datetime_str_2, MASK) - datetime.strptime(datetime_str_1, MASK)).days

difference = timedelta_days('2019/05/10 00:00:00', '2019/10/04 00:00:00')
