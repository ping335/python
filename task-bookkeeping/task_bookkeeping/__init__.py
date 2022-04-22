from datetime import date, datetime, timedelta
import sys


from task_bookkeeping import storage
from task_bookkeeping.helpers import (
	prompt, input_int, input_date, input_datetime,
	print_table, print_pay
)

from task_bookkeeping.services import make_db_connection


def input_pay():
	"""Запрашивает индектификатор задачи и возвращает ее из БД"""
	def cb(pay_id):
		with make_db_connection() as conn:
			pay = storage.get_pay(conn, int(pay_id))
			
			if pay is None:
				raise ValueError(f'Платеж с ID {pay_id} не найден.')
				
			return pay
			
	return prompt('Введите ID платежа', type_cast=cb)


def input_pay_data(pay=None):
	"""Запрашивает данные от пользователя о платеже и возвращает ввод"""
	pay = dict(pay) if pay else {}
	data = {}
	
	data['title'] = prompt('Название', default=pay.get('title', ''))
	data['price'] = prompt('Цена', default=pay.get('price', 0.0))
	data['quantity'] = prompt(
		'Количество', 
		default=pay.get('quantity', 1)
	)
	#data['pay_date'] = input_datetime(
	#	'Дата платежа',
	#	default=pay.get('pay_date', datetime.now())
	#)
	
	return data


def action_list_pays(): #походу надо переделать
	"""Вывести список плтажей"""


def action_show_pay():
	"""Просмотреть платеж"""
	pay = input_pay()
	
	if pay is not None:
		print_pay(pay)


def action_add_pay():
	"""Добавить платеж"""
	with make_db_connection() as conn:
		data = input_pay_data()
		storage.create_payment(conn, **data)
		print(f'Платеж "{data["title"]}" успешно осуществлен.')


def action_edit_pay():
	"""Отредактировать платеж"""
	pay = input_pay()
	
	if pay is not None:
		with make_db_connection() as conn:
			data = input_pay_data(pay)
			storage.update_payment(conn, pay['id'], **data)
			print(f'Платеж "{data["title"]}" успешно отредактирован.')


def action_output_all_pay():
	"""Вывести все платежи"""


def action_output_all_pay_for_period():
	"""Вывести все платежи за указанный период"""


def action_output_top_largest_pay():
	"""Вывести топ самых крупных платежей"""


def action_show_menu():
	"""Показать меню"""
	for cmd, action_tuple in actions.items():
		print(f'{cmd}. {action_tuple[1]}')


def show_usage():
	"""Показать как использовать"""
	commands = ', '.join(actions.keys())
	print(f'\nНеизвестная команда.\nВведите одну из: {commands}')


actions = {
	'1': (action_add_pay, 'Добавить платеж'),
	'2': (action_edit_pay, 'Отредактировать платеж'),
	'3': (action_output_all_pay, 'Вывести все платежи'),
	'4': (action_output_all_pay_for_period, 'Вывести все платежи за указанный период'),
	'5': (action_output_top_largest_pay, 'Вывести топ самых крупных платежей'),
	'm': (action_show_menu, 'Показать меню'),
	'q': (sys.exit, 'Закрыть программу'),
}


def main():
	with make_db_connection() as conn:
		storage.initialize(conn, 'schema.sql')
	
	action_show_menu()
	
	while 1:
		cmd = input('\nВведите команду: ').strip()
		
		action_tuple = actions.get(cmd, (show_usage, ''))
		action_tuple[0]()
