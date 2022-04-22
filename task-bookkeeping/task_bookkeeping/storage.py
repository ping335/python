"""
Модуль, который содержит функции для работы с постоянным хранилищем 
"""
from datetime import datetime, time


SQL_CREATE_NEW_PAYMENT = 'INSERT INTO task (title, price, quantity) VALUES (?, ?, ?)'

SQL_UPDATE_PAYMENT = 'UPDATE task SET title=?, price=?, quantity=?, pay_date=? WHERE id=?'

SQL_SELECT_ALL_PAYMENTS = 'SELECT id, title, price, quantity, pay_date FROM task'

SQL_SELECT_PAYMENTS_PER_DATE = f'{SQL_SELECT_ALL_PAYMENTS} WHERE pay_date BETWEEN ? AND ?'

SQL_SELECT_PAYMENT_BY_ID = f'{SQL_SELECT_ALL_PAYMENTS} WHERE id=?'

'''
написать еще один запрос Вывести топ самых крупных плдатежей
запрос на сортировку и ограничение
'''

def initialize(conn, creation_schema):
    """Используя переданный SQL-скрипт, инициализирует структуру БД."""
    with open(creation_schema) as f:
        conn.executescript(f.read())


def create_payment(conn, title, price, quantity):
    """Сохраняет новый платеж в БД."""
    conn.execute(SQL_CREATE_NEW_PAYMENT, (title, price, quantity))


def update_payment(conn, pay_id, title, price, quantity, pay_date):
	"""Обновляет платеж в БД"""
	conn.execute(SQL_UPDATE_PAYMENT, (title, price, quantity, pay_date, pay_id))


def get_pay(conn, pay_id):
	"""Выбирает и возвращает из БД платеж с указанным первичным ключом"""
	return conn.execute(SQL_SELECT_PAYMENT_BY_ID, (pay_id,)).fetchone()


'''а мне нужно две даты'''
def get_payments_per_date(conn, dt):
	"""Возвращает платежи за указанную дату"""
	dt = datetime.combine(dt, time())
	dt_end = datetime.combine(dt, time(23,59,59))
	
	return conn.execute(SQL_SELECT_PAYMENTS_PER_DATE, (dt, dt_end)).fetchall()

def get_all_payments(conn):
	""""Возвращает все платежи из БД"""
	return conn.execute(SQL_SELECT_ALL_PAYMENTS).fetchall()
