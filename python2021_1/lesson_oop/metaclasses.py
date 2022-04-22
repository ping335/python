"""
Метаклассы

Класс - шаблон для создания объекта.
Метакласс - шаблон для создания класса.

По-умолчанию для всех классов базовым метаклассом является type.

“Metaclasses are deeper magic than 99% of users should ever worry about.
If you wonder whether you need them, you don’t
(the people who actually need them know with certainty that they need them,
and don’t need an explanation about why).”
— Tim Peters
"""


class DemoMeta(type):
    def __new__(mcs, name, bases, d):
        print('Выделение памяти под класс:\n', name, bases, d)
        return super().__new__(mcs, name, bases, d)
    
    def __init__(cls, name, bases, d):
        print('Инициализация класса:\n', name, bases, d)
        super().__init__(name, bases, d)
    
    def __call__(cls, *args, **kwargs):
        print('Создание экземпляра/объекта:\n', args, kwargs)
        return super().__call__(*args, **kwargs)


class DemoClass(metaclass=DemoMeta):
    def __new__(cls, *args, **kwargs):
        # НИКОГДА не переопределяем!!!
        print('Выделение памяти под экземпляр/объект:\n', args, kwargs)
        return super().__new__(cls)
    
    def __init__(self, *args, **kwargs):
        print('Инициализация экземпляра/объекта:\n', args, kwargs)


print('======')
obj = DemoClass(1, 2, a=3, b=4, c=5)
print('======')
obj2 = DemoClass('Test')





