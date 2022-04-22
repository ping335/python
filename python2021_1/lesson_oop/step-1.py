"""
Классы и объекты

Объект состоит из:
1. Свойства или данные
2. Методы или поведение

self - ссылка на текущий объект/экземпляр

Модификаторы доступа:
public    - доступ из любой области
            в Python все public
protected - доступ внутри класса и классов-наследников
            _prop   => защищенное св-во
            _method => защищенный метод
private   - доступ только внутри класса, где объявлен
            __prop   => закрытое св-во
            __method => закрытый метод
            
class A:
    def __init__(self, value):
        self._value = value
    
    def get_value(self):
        # Getter - получатель - возвращает значение св-ва
        return self._value
    
    def set_value(self, value):
        # Setter - установщик - задает новое значение для св-ва
        self._value = value
"""

# todo: Как создать класс?

class Employee:
    """Сотрудник"""
    
    def __init__(self, firstname, lastname, hours_worked, salary_strategy):
        """
        Это конструктор.
        Основная и единственная цель конструктора - инициализировать объект.
        """
        self._firstname = firstname
        self._lastname = lastname
        self._hours_worked = None
        self.set_hours_worked(hours_worked)
        self._salary_strategy = salary_strategy
    
    def get_fullname(self):
        """Возвращает полное имя сотрудника."""
        return f'{self._firstname} {self._lastname}'
    
    def get_hours_worked(self):
        return self._hours_worked
    
    def set_hours_worked(self, hours_worked):
        if hours_worked <= 0:
            raise ValueError('Количество часов должно быть положительным числом.')
        self._hours_worked = hours_worked
    
    def calculate_salary(self):
        """Считает и возвращает зарплату сотрудника."""
        return self._salary_strategy.calculate(self.get_hours_worked())


# todo: Что такое наследование?

class SalaryStrategy:
    """Стратегия оплаты труда."""
    
    def calculate(self, hours_worked):
        """Считает размер заработной платы."""
        raise NotImplementedError


class HourlyPaymentStrategy(SalaryStrategy):
    """Почасовая оплата. (Wage)"""
    
    def __init__(self, cost_per_hour):
        self._cost_per_hour = cost_per_hour
    
    def calculate(self, hours_worked):
        # вызов родительского метода
        # super().calculate(hours_worked) # НО, в данном примере не нужен!
        return round(self._cost_per_hour * hours_worked, 2)


class FixedRateStrategy(SalaryStrategy):
    """Фиксированная ставка (оклад)"""
    
    def __init__(self, salary):
        self._salary = salary
    
    def calculate(self, hours_worked):
        days = hours_worked / 8
        return round(self._salary * days / 22, 2)
    

# todo: Как создать объект?

hourly_wage = HourlyPaymentStrategy(1500)
# hourly_wage = FixedRateStrategy(35000)
person1 = Employee('Василий', 'Пупкин', 10, hourly_wage)
# person1.firstname = 'Василий' # присвоение/установка значения св-ва

# print(person1)
# print(person1.firstname)      # получение значения св-ва
# print(person1.get_fullname()) # вызов метода
print(f'Зарплата {person1.get_fullname()} составила {person1.calculate_salary()}')

person2 = Employee('Билл', 'Гейтц', 100500, FixedRateStrategy(15000))
# print(person2)
# print(person2.get_fullname()) # вызов метода
print('Зарплата {} составила {}'.format(
    person2.get_fullname(), person2.calculate_salary()
))

# person3 = Employee('Linus', 'Torvalds', 8, SalaryStrategy())
# person3.calculate_salary()


# todo: Как объявить статическое свойство или метод?

class Car:
    def __init__(self, number):
        self._number = number
    
    def get_number(self):
        return self._number


class CarFactory:
    """Статическая фабрика."""
    
    __cars = {}
    
    @classmethod
    def get(cls, number):
        return cls.__cars.get(number)
    
    @classmethod
    def create(cls, number):
        if number in cls.__cars:
            raise ValueError(f'Автомобиль с номером {number} уже существует!')
        
        cls.__cars[number] = car = Car(number)
        return car


car1 = CarFactory.create('а007аа')
car2 = CarFactory.get('а007аа')
print(car1 is car2)

car3 = CarFactory.create('а007аа')





