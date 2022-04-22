"""
Модуль содерижит вспомогательные функции,
для которых создавать отдельный модуль не рационально.
"""

from datetime import datetime


__all__ = (
    'prompt', 'input_int', 'input_float',
    'input_datetime', 'input_date',
    'print_table', 'print_task',
)


def prompt(msg, default=None, type_cast=None):
    """Запрашивает данные от пользователя и возвращает ввод."""
    while 1:
        value = input(f'{msg}: ')
        
        if not value:
            return default
        
        if type_cast is None:
            return value
        
        try:
            return type_cast(value)
        except ValueError as err:
            print(err)


def input_int(msg='Введите число', default=None):
    """Запрашивает целое число от пользователя и возвращает ввод."""
    return prompt(msg, default, type_cast=int)


def input_float(msg='Введите число', default=None):
    """Запрашивает дробное число от пользователя и возвращает ввод."""
    return prompt(msg, default, type_cast=float)


def input_datetime(msg='Введите дату', default=None, fmt='%Y-%m-%d %H:%M:%S'):
    """Запрашивает дату и время от пользователя и возвращает ввод."""
    return prompt(msg, default, type_cast=lambda value: datetime.strptime(value, fmt))


def input_date(msg='Введите дату', default=None, fmt='%Y-%m-%d'):
    """Запрашивает дату от пользователя и возвращает ввод."""
    return prompt(
        msg,
        default,
        type_cast=lambda value: datetime.strptime(value, fmt).date()
    )


def print_table(headers, iterable):
    """Распечатывает таблицу на экран."""
    print(' | '.join(headers.values()))
    
    for row in iterable:
        data = []
        
        for col_name in headers:
            data.append(row[col_name])
        
        print(' | '.join(map(str, data)))


def print_pay(pay):
    """Распечатывает платеж на экран."""
    print(f'''
    ----------------------------------------------------------------
               Наименование платежа: "{pay['title']}"
			Цена (за единицу товара или услугу): {pay['price']}
					Количество: {pay['quantity']}
			Дата платежа: {pay['pay_date']:%d.%m.%Y в %H:%M}
    ----------------------------------------------------------------
''')
