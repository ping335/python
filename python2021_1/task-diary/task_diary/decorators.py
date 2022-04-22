"""
Модуль хранит все декораторы
"""
from functools import wraps

from task_diary.services import make_db_connection


def with_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with make_db_connection() as conn:
            return func(conn, *args, **kwargs)
    return wrapper
