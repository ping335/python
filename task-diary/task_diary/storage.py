"""
Модуль, который содержит функции для работы с постоянным хранилищем.
"""

from datetime import datetime, time


SQL_CREATE_NEW_TASK = 'INSERT INTO task (title, planned, description) VALUES (?, ?, ?)'

SQL_UPDATE_TASK = 'UPDATE task SET title=?, planned=?, description=? WHERE id=?'

SQL_UPDATE_TASK_STATUS = 'UPDATE task SET done=? WHERE id=?'

SQL_SELECT_ALL_TASKS = 'SELECT id, title, planned, description, done, created FROM task'

SQL_SELECT_TASKS_PER_DATE = f'{SQL_SELECT_ALL_TASKS} WHERE planned BETWEEN ? AND ?'

SQL_SELECT_TASK_BY_ID = f'{SQL_SELECT_ALL_TASKS} WHERE id=?'


def initialize(conn, creation_schema):
    """Используя переданный SQL-скрипт, инициализирует структуру БД."""
    with open(creation_schema) as f:
        conn.executescript(f.read())


def create_task(conn, title, planned, description=''):
    """Сохраняет новую задачу в БД."""
    conn.execute(SQL_CREATE_NEW_TASK, (title, planned, description))


def update_task(conn, task_id, title, planned, description=''):
    """Обновляет задачу в БД."""
    conn.execute(SQL_UPDATE_TASK, (title, planned, description, task_id))


def update_task_status(conn, task_id, status):
    """Обновляет статус задачи и сохраняет в БД."""
    conn.execute(SQL_UPDATE_TASK_STATUS, (status, task_id))


def get_task(conn, task_id):
    """Выбирает и возвращает из БД задачу с указанным первичным ключом."""
    return conn.execute(SQL_SELECT_TASK_BY_ID, (task_id,)).fetchone()


def get_tasks_per_date(conn, dt):
    """Возвращает задачи за указанную дату."""
    dt = datetime.combine(dt, time())
    dt_end = datetime.combine(dt, time(23, 59, 59))
    return conn.execute(SQL_SELECT_TASKS_PER_DATE, (dt, dt_end)).fetchall()


def get_all_tasks(conn):
    """Возвращает все задачи из БД."""
    return conn.execute(SQL_SELECT_ALL_TASKS).fetchall()
