"""
Шаг №1 - Дополняем работу функции, не изменяя оригинальную
"""


# todo: Объявляем функцию
def say_hello():
    return 'Hello'


# todo: Функция-обертка, которая ничего не делает
def null_decorator(func):
    return func


# todo: Функция-обертка, которая добавляет восклицательный знак
def exclaim_decorator(func):
    def wrapper():
        return func() + '!'
    return wrapper


print(say_hello, type(say_hello))

say_hello = null_decorator(say_hello)
print(say_hello, type(say_hello))
print(say_hello())

say_hello = exclaim_decorator(say_hello)
print(say_hello, type(say_hello))
print(say_hello())
