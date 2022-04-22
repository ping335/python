"""
todo: Если имя атрибута - переменная

hasattr(obj, name)
getattr(obj, name[, default])
setattr(obj, name, value)
delattr(obj, name)


todo: Как динамически создать класс?

type(obj)
type(name, bases, dict)
    - name
        имя нового типа (имя класса)
        будет значением __name__
    - bases
        кортеж базовых типов (от кого наследуем)
        будет значением __bases__
    - dict
        словарь атрибутов создаваемого типа
        будет значением __dict__


todo: Специальные свойства и методы классов

__name__        - имя класса, метода, функции
__module__      - имя модуля
__qualname__    - полное имя класса, метода, функции (>=3.3)
__doc__         - строка документации
__class__       - объект-метакласс
__bases__       - кортеж базовых классов
__dict__        - словарь атрибутов класса
__mro__         - кортеж с родительскими типами, выстроенными в порядке разрешения методов

todo: Специальные свойства и методы объектов

__class__  -  объект-класс, экземпляром которого является данный объект
__dict__   - словарь атрибутов объекта (не создается, если используем __slots__)

__dir__()  - список атрибутов класса, используется функцией dir()
"""

print(type([]), type(list), type(type))


def init_point(self, x, y):
    self.x = x
    self.y = y

Point = type('Point', (), {
    '__init__': init_point,
    '__repr__': lambda self: f'Point({self.x}, {self.y})',
})

print(Point, type(Point))

rect_top = Point(0, 0)
rect_bottom = Point(10, 5)
print(rect_top, rect_bottom)







