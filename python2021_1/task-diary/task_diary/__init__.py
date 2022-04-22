from collections import namedtuple
from datetime import date, datetime, timedelta
import importlib.resources # >= 3.7 importlib_resources
import sys

from task_diary import storage
from task_diary.helpers import (
    prompt, input_int, input_date, input_datetime,
    print_table, print_task
)


Action = namedtuple('Action', ('func', 'title'))
actions = {}


def menu_action(cmd, title=None):
    def decorator(func):
        actions[str(cmd)] = Action(
            func,
            title or str(func.__doc__).strip().splitlines().pop(0)
        )
        return func
    return decorator


def input_task():
    """Запрашивает идентификатор задачи и возвращает ее из БД."""
    def cb(task_id):
        task = storage.get_task(int(task_id))
        
        if task is None:
            raise ValueError(f'Задача с ID {task_id} не найдена.')
        
        return task
    
    return prompt('Введите ID задачи', type_cast=cb)


def input_task_data(task=None):
    """Запрашивает данные от пользователя о задаче и возвращает ввод."""
    task = dict(task) if task else {}
    data = {}
    
    data['title'] = prompt('Название', default=task.get('title', ''))
    
    data['planned'] = input_datetime(
        'Запланировано',
        default=task.get('planned', datetime.now() + timedelta(days=1))
    )
    
    data['description'] = prompt('Описание', default=task.get('description', ''))
    
    return data


@menu_action(1)
def action_list_tasks():
    """Вывести список задач"""
    planned = input_date('Введите дату', date.today())    
    tasks = storage.get_tasks_per_date(planned)
    print_table({
        'id': 'ID',
        'title': 'Название',
        'planned': 'Запланировано',
        'done': 'Выполнено',
    }, tasks)


@menu_action(2)
def action_show_task():
    """Просмотреть задачу"""
    task = input_task()
    
    if task is not None:
        print_task(task)


@menu_action(3)
def action_add_task():
    """Добавить задачу"""
    data = input_task_data()
    storage.create_task(**data)
    print(f'Задача "{data["title"]}" успешно создана.')


@menu_action(4)
def action_edit_task():
    """Отредактировать задачу"""
    task = input_task()
    
    if task is not None:
        data = input_task_data(task)
        storage.update_task(task['id'], **data)
        print(f'Задача "{data["title"]}" успешно отредактирована.')


@menu_action(5)
def action_done_task():
    """Завершить задачу"""


@menu_action(6)
def action_reopen_task():
    """Начать задачу заново"""


@menu_action('m')
def action_show_menu():
    """Показать меню"""
    for cmd, action_tuple in actions.items():
        print(f'{cmd}. {action_tuple.title}')


def show_usage():
    """Показать, как использовать"""
    commands = ', '.join(actions.keys())
    print(f'\nНеизвестная команда.\nВведите одну из: {commands}')


def main():
    creation_script = importlib.resources.read_text('task_diary.resources', 'schema.sql')
    storage.initialize(creation_script)
    
    actions['q'] = Action(sys.exit, 'Выйти')
    
    action_show_menu()
    
    while 1:
        cmd = input('\nВведите команду: ').strip()
        
        action_tuple = actions.get(cmd, Action(show_usage, ''))
        action_tuple.func()
