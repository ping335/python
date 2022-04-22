from datetime import date, datetime, timedelta
import sys

from task_diary import storage
from task_diary.helpers import (
    prompt, input_int, input_date, input_datetime,
    print_table, print_task
)
from task_diary.services import make_db_connection


def input_task():
    """Запрашивает идентификатор задачи и возвращает ее из БД."""
    def cb(task_id):
        with make_db_connection() as conn:
            task = storage.get_task(conn, int(task_id))
            
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


def action_list_tasks():
    """Вывести список задач"""
    planned = input_date('Введите дату', date.today())
    
    with make_db_connection() as conn:
        tasks = storage.get_tasks_per_date(conn, planned)
        print_table(
            {
                'id': 'ID',
                'title': 'Название',
                'planned': 'Запланировано',
                'done': 'Выполнено',
            },
            tasks
        )


def action_show_task():
    """Просмотреть задачу"""
    task = input_task()
    
    if task is not None:
        print_task(task)


def action_add_task():
    """Добавить задачу"""
    with make_db_connection() as conn:
        data = input_task_data()
        storage.create_task(conn, **data)
        print(f'Задача "{data["title"]}" успешно создана.')


def action_edit_task():
    """Отредактировать задачу"""
    task = input_task()
    
    if task is not None:
        with make_db_connection() as conn:
            data = input_task_data(task)
            storage.update_task(conn, task['id'], **data)
            print(f'Задача "{data["title"]}" успешно отредактирована.')


def action_done_task():
    """Завершить задачу"""


def action_reopen_task():
    """Начать задачу заново"""


def action_show_menu():
    """Показать меню"""
    for cmd, action_tuple in actions.items():
        print(f'{cmd}. {action_tuple[1]}')


def show_usage():
    """Показать, как использовать"""
    commands = ', '.join(actions.keys())
    print(f'\nНеизвестная команда.\nВведите одну из: {commands}')


actions = {
    '1': (action_list_tasks, 'Вывести список задач'),
    '2': (action_show_task, 'Просмотреть задачу'),
    '3': (action_add_task, 'Добавить задачу'),
    '4': (action_edit_task, 'Отредактировать задачу'),
    '5': (action_done_task, 'Завершить задачу'),
    '6': (action_reopen_task, 'Начать задачу заново'),
    'm': (action_show_menu, 'Показать меню'),
    'q': (sys.exit, 'Выйти'),
}


def main():
    with make_db_connection() as conn:
        storage.initialize(conn, 'schema.sql')
    
    action_show_menu()
    
    while 1:
        cmd = input('\nВведите команду: ').strip()
        
        action_tuple = actions.get(cmd, (show_usage, ''))
        action_tuple[0]()
