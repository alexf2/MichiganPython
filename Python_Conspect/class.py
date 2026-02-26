class Employee:
    vacation_days = 28  # class field

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name  # instance field
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


class FullTimeEmployee(Employee):

    def get_unpaid_vacation(self, start_date, days):
        return (f'Начало неоплачиваемого отпуска: {start_date}, '
                f'продолжительность: {days} дней.')


class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days

# --------------------------------


class A:
    def __init__(self):
        self.__attr = 0

    def __method(self):
        print("A.__attr", self.__attr)


class B(A):
    def __init__(self):
        super().__init__()
        self.__attr = 1  # Doesn't override A.__attr

    def __method(self):  # Doesn't override A.__method()
        print("B.__attr", self.__attr)
