class Robot:
    # Состояние батареи базовой станции:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    # Декорируем и изменяем метод update_base_battery_status(),
    # чтобы менять значение атрибута не в объекте, а в классе:
    @classmethod
    def update_base_battery_status(cls, new_status):  # Указываем аргумент cls.
        """
        Обновляет состояние батареи базовой станции.
        """
        # Присваиваем новое значение атрибуту класса.
        cls.base_battery_status = new_status

    def report(self):
        """
        Печатает в консоли состояние батареи базовой станции.
        """
        print(f'{self.name} reporting: Battery status is {self.base_battery_status}%')

    @staticmethod
    def predict_battery_lifetime(current_capacity, charge_cycles):
        """
        Прогнозирует срок службы аккумулятора 
        на основе текущей ёмкости и количества циклов зарядки.
        """
        # Пусть максимальная ёмкость нового аккумулятора будет равна 5000 мАч
        max_capacity = 5000
        return (current_capacity / max_capacity) * (1000 - charge_cycles)


# Создаем двух роботов:
robot1 = Robot('R2-D2')
robot2 = Robot('C-3PO')

# Печатаем состояние батареи:
robot1.report()
robot2.report()

# Обновляем статус батареи в классе: обращаемся не к объекту, а к классу.
Robot.update_base_battery_status(80)

# Снова печатаем состояние батареи:
robot1.report()
robot2.report()
