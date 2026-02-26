english_words = ['apple', 'banana', 'cherry', 'date', 'fig']
# Объект english_words итерируемый?
print(iter(english_words))

quantity = 5
# Объект quantity итерируемый?
print(iter(quantity))

english_words = ['apple', 'banana', 'cherry', 'date', 'fig']
# У объекта english_words есть метод __iter__?
print('__iter__' in dir(english_words))


english_words = ['apple', 'banana', 'cherry', 'date', 'fig']
# «Положить» в переменную 'a' объект итератора.
a = iter(english_words)
# У объекта итератора, который «лежит» в переменной 'а'
# есть метод '__next__'?
print('__next__' in dir(a))
# Обратиться к одному элементу итерируемого объекта...
print(a.__next__())
# Обратиться к следующему элементу итерируемого объекта.
print(a.__next__())


class MyRange:
    def __init__(self, start, end):
        # Установить начальное значение последовательности. 
        self.current = start
        # Установить конечное значение последовательности.
        self.end = end
    
    # Метод, который возвращает сам объект (self) в качестве итератора.
    def __iter__(self):
        return self
    
    # Метод, который реализует логику получения следующего 
    # элемента последовательности.
    def __next__(self):
        # Если начальное значение последовательности меньше или равно 
        # конечному значению...
        if self.current <= self.end:
            # ...вернуть текущее значение...
            value = self.current
            # ...и увеличить его на 1.
            self.current += 1
            return value
        # Иначе...
        else:
            # выбросить исключение StopIteration, чтобы указать, 
            # что элементы в последовательности закончились.
            raise StopIteration
