"""Исключения"""

try:
    # код, в котором потенциально может появиться исключение
    a = input()
    
    if a.isdigit():
        a = int(a)
    else:
        print('Вы ввели не число')
    
    b = int(input())
    
    print(a + b)
except ValueError:
    # обработка исключения
    print('Вы ввели не число')
except TypeError as err:
    print(err)
except (ImportError, ArithmeticError):
    pass
except:
    print('Все ошибки')
else:
    print('Выпоняется, если не было ошибок')
finally:
    print('Этот блок выполняется всегда')
