"""
Шаг №2 - Аргументы функции
"""

def greeting_username(name):
    return f'Hello, {name}'


def goodbye(firstname, lastname):
    return f'Good bye, {firstname} {lastname}'


def exclaim_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + '!'
    return wrapper


greeting_username = exclaim_decorator(greeting_username)
print(greeting_username, type(greeting_username))

print(greeting_username('Вася'))
print(greeting_username('Петя'))

goodbye = exclaim_decorator(goodbye)
print(goodbye('Василий', 'Пупкин'))
