"""
Генераторы

Генератор – это функция, которая воспроизводит последовательность значений
и может использоваться при выполнении итераций.

Инструкция yield возвращает результат,
и выполнение функции приостанавливается в этой точке,
пока снова не будет вызван метод __next__().
После этого выполнение функции возобновляется, начиная с инструкции,
следующей за инструкцией yield.

Функция-генератор сигнализирует о завершении последовательности значений
и прекращении итераций, возбуждая исключение StopIteration.
Для генераторов считается недопустимым по завершении итераций возвращать значение,
отличное от None (return "Сообщение об ошибке").
"""

from urllib.request import urlopen


def generator():
    print('Шаг №1')
    yield 1
    print('Шаг №2')
    yield 2
    print('Шаг №3')

g = generator()
print(g, type(g))
print(next(g))
print(next(g))
# print(next(g))


def countdown(n, step=1):
    print('Генератор стартовал!')
    while n > 0 and step > 0:
        yield n
        n -= step


for i in countdown(5, -2):
    print(i)


def iter_pages(urls):
    for url in urls:
        yield urlopen(url).read()


pages = iter_pages(['http://python.org', 'http://ya.ru'])
for source in pages:
    print(source)



