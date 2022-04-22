"""
Перегрузка операторов
"""

class Vector:
    __slots__ = ('x', 'y') # __dict__ больше не создается
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        """Неявно вызывается функцией repr(obj)"""
        return f'{self.__class__.__name__}({self.x}, {self.y})'
    
    def __add__(self, other):
        """Перегрузка оператора +"""
        return self.__class__(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Перегрузка оператора -"""
        return self.__class__(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        """Перегрузка оператора *"""
        return self.__class__(self.x * other.x, self.y * other.y)
    
    def __gt__(self, other):
        """Перегрузка оператора >"""
        return self.length > other.length
    
    def __eq__(self, other):
        """Перегрузка оператора =="""
        return self.length == other.length
    
    def __ge__(self, other):
        """Перегрузка оператора >="""
        return self.length >= other.length
    
    @property
    def length(self):
        """Длина вектора"""
        return (self.x ** 2 + self.y ** 2) ** .5
    
    # @length.setter
    # def length(self, value):
    #     """Присвоить значение св-ву"""
    # 
    # @length.deleter
    # def length(self):
    #     """Удалить св-во"""



v1 = Vector(-3, 4)
v2 = Vector(-3, 6)
print(f'Сумма векторов: {v1} + {v2} = {v1 + v2}')
print(f'Разность векторов: {v1} - {v2} = {v1 - v2}')
print(f'Произведение векторов: {v1} * {v2} = {v1 * v2}')
print(f'Длина вектора {v1} = {v1.length}')







