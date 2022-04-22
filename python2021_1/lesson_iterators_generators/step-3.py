"""
Генераторы списков/множеств/словарей.
(list comprehensions)

[expression for item1 in iterable1 if condition1
            for item2 in iterable2 if condition2
            ...
            for itemN in iterableN if conditionN]
"""

numbers = [1, 2, 3, 3, 2, 1]

"""
squares = []
for i in numbers:
    squares.append(i * i)
"""
squares = [i * i for i in numbers]
odd = [i for i in numbers if i % 2]

"""
points = []
for x in range(3):
    for y in range(2):
        points.append((x, y))
"""
points = [(x, y) for x in range(3) for y in range(2)]

print(squares, odd, points)


# todo: Генераторы множеств

s = {i for i in numbers} # сложно!!! set(numbers)
print(s)

text = 'Python is programming language!'
words_lengths = {len(word) for word in text.split()}
print(f'''
Уникальные длины слов: {words_lengths}
Самое короткое слово:  {min(words_lengths)}
Самое длинное слово:   {max(words_lengths)}
''')


# todo: Генераторы словарей

keys = ['id', 'origin_url', 'short_url']
values = [1, 'http://python.org', '/1']
# так делать нельзя!!!!
# data = {k: v for i, k in enumerate(keys) for j, v in enumerate(values) if i == j}
data = dict(zip(keys, values))
print(data)

users = [
    {
        'id': 1,
        'name': 'Linus Torvalds',
        'skills': ('C++', 'Linux'),
        'is_developer': True,
    },
    {
        'id': 2,
        'name': 'Richard Stallman',
        'skills': ('C', 'GNU'),
        'is_developer': True,
    },
    {
        'id': 1,
        'name': 'Linus Torvalds',
        'skills': ('C++', 'Linux'),
        'is_developer': True,
    },
]

users = {user['id']: user for user in users}
print('\n', users)


# todo: Выражения-генераторы или генераторные выражения

squares_generator = (i * i for i in numbers)
print(squares_generator, tuple(squares_generator), set(squares_generator))

with open(__file__) as f:
    lines = (line.strip() for line in f)
    todos = (s for s in lines if s.startswith('# todo:'))
    print('First todo:', next(todos))
    print('Todos:', todos, list(todos))


# todo: Примеры

print('; '.join(str(i) for i in numbers))

squares = list(map(lambda i: i * i, numbers))
odd = list(filter(lambda i: i % 2, numbers))
print(squares, odd)

squares_sum = sum(i * i for i in numbers)
print(squares_sum)
















