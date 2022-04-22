"""
Ввод и вывод

todo: Стандартный потоки ввода/вывода

№0 - stdin - стандартный поток ввода
     input(), sys.stdin
№1 - stdout - стандартный поток вывода
     print(), sys.stdout
№2 - stderr - стандартный поток ошибок
     traceback, sys.stderr


todo: Файловый ввод и вывод

open(filename [, mode='r'])

Режимы записи:
    w - перезапись
        если файл существует, то он будет перезаписан (затерт)
        если файл не существует, то он создается
    a - append - добавление/дозапись в конец файла
        если файл существует, то запись произойдет в конец файла
        если файл не существует, то он создается
    x - эксклюзивное создание файла
        если файл существует, то будет возбуждено исключение
        если файл не существует, то он создается

Режимы чтения:
    r - чтение, режим по-умолчанию
    w+
    a+

t - текстовый режим (по-умолчанию) - str
b - двоичный режим                 - bytes
"""

# todo: Как открыть файл в режиме записи?
f = open('out.txt', 'w')

try:
    # todo: Как записывать в файл?
    f.write('01234\n') # только строки!!!
    f.write('56789\n')
    f.writelines(['A\n', 'B\n'])
    # f.write('''
    #     1.
    #         2.
    #             3.
    # ''')
finally:
    # todo: Как закрыть файл?
    f.close()


# todo: Как открыть файл в режиме чтения?
f = open('out.txt') # default 'r'

try:
    # todo: Как прочитать файл в строку?
    s = f.read()
    print(f'Прочитать файл в строку:\n{s}')
    
    # todo: Как узнать текущую позицию курсора?
    pos = f.tell()
    print(f'Текущая позиция курсора: {pos}')
    
    # todo: Как изменить позицию курсора?
    f.seek(0)
    
    # todo: Как прочитать файл в список?
    lines = f.readlines()
    print(f'Прочитать файл в список:\n{lines}')
    
    # todo: Как прочитать файл построчно?
    f.seek(0)
    
    line_1 = f.readline().strip()
    line_2 = f.readline().strip()
    print(f'Прочитать файл построчно:\n{line_1}\n\n{line_2}')
    
    for line in f:
        print(line.strip())
    
    # todo: Как прочитать из файла N байт?
    f.seek(0)
    result = f.read(4)
    print(f'Прочитать из файла 4 байта: {result}')
finally:
    f.close()


# todo: Контекстный менеджер
# При работе с файлом всегда!!!! используем
with open('out.txt') as f, open(__file__) as lesson:
    print(f.read())
    print(lesson.read())

# print(f.read())




