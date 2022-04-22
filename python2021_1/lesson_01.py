# Однострочный комментарий

'''
Многострочный
комментарий
'''

"""
todo: Как объявить переменную в Python?


"""

is_student = True
hours = 5
price = 255.99
name = 'Python 3'

result = None
result = 1

# todo: bool
flag1 = True
flag2 = False

# todo: int
i1 = 1066
i2 = 0b101 # Двоичная СС
i3 = 0o255 # Восьмеричная СС
i4 = 0xFF  # Шестнадцатиричная СС
i5 = 0xff

print(i1, i2, i3, i4, i5)

# todo: float
f1 = 12.3
f2 = 2e6   # 2 * 10 ** 6
f3 = 12e-3 # 12 * 10 ** -3 => 0.012

# todo: complex
c1 = complex(2, 3) # => 2+3j
c2 = 2+3j
c3 = 3.14j
print(c2.real, c2.imag)
print(c3.conjugate()) # сопряженное число
c4 = c3.conjugate()
print(c4)

# todo: str

s1 = 'Hello, Python!'
s2 = "\tHello, Python!\n"
s3 = '\' " \\ '
s4 = "\" ' "
s5 = " ' "
s6 = '''
Многострочный
текст
'''
s7 = """\"""
    \t"Многострочный"
        'текст'
"""
print(s3, s4, s7)

s8 = r'^\d+$' # сырые строки

# todo: bytes

b1 = b'Hello, Python'
b2 = bytes('Привет, Питон!', 'utf-8')
print(b1, b2)


# todo: tuple
t1 = (1, 2, 3, 1.5, True, (4, 5, 6))
print(t1[3], t1[5][0])
# t1[4] = False
t2 = ('Hi',)
print(t2)
person = ('Вася', 45, True)

# todo: list
lst1 = [1, 2, 3, 1.5, True, (4, 5, 6)]
lst1[4] = False
print(lst1)


# todo: set
set1 = {9, 8, 7, 7, 8, 9}
set1.add(10)
set1.update({True, 1, 0, False})
print(set1)

empty_set = set()
print(empty_set)

# dict
person = {
    'name': 'Вася',
    'age': 45,
    'is_developer': True,
}
person['age'] = 40
person['skills'] = ('Python', 'JavaScript')
del person['age']
print(person)
print(person['name'], person['skills'])


emty_dict = {}


# todo: Как определить тип переменной Python?
print(
    type(flag1),
    type(i1),
    type(person),
    type(None)
)

"""
todo: Как выполнить явное приведение переменной к определенному типу?

bool(x)
int(x, [, base])
float(x)
complex(real [, imag])
str(x)
tuple(x)
list(x)
set(x)
dict(x)
"""

"""
todo: Какие операторы существуют в Python?

Арифметические:  + - * / % // **
Сравнения:       == != > < >= <=
Логические:      and or not
Побитовые:       & | ~ ^ << >>
Присваивания:    = += -= *= /= %= //= **= &= |= ^= <<= >>=
Принадлежности:  in, not in
Тождественности: is, is not
"""

i = 1
i += 1

# todo: Ветвление

a = 1
b = 2

if a > b:
    print('a > b')
elif a == b:
    print('a = b')
else:
    # pass
    print('a < b')


# todo: Тернарный оператор

# number = input()
# number = int(number) if number.isdigit() else 0
# print(number)


# todo: Циклы

i = 1

while i:
    if not i % 2:
        print(i)
    
    if i == 10:
        break

    i += 1


lst = [1, 2, 3]

for j in lst:
    print(j)

for i in range(1, -11, -2):
    print('=>', i)

s = 'Hello'

for c in enumerate(s):
    print(c)

for index, char in enumerate(s):
    print(index, char)

for key, value in person.items():
    print(key, '=>', value)


lst = [(1, 2, 3), (4, 5, 6)]

for a, b, c in lst:
    print(a, b, c)
