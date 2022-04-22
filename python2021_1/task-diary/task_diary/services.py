"""
Модуль содержит функции, которые предоставляют внешние сервисы(ресурсы).
"""

from configparser import ConfigParser
from datetime import datetime
import importlib.resources
import os
import sqlite3

from task_diary import resources
from task_diary.helpers import user_config_dir, user_data_dir


def make_config(*config_files):
    """Читает конфигурационные файлы и возвращает объект ConfigParser."""
    config = ConfigParser()
    config.read(config_files)
    return config


def make_default_config():
    """Читает конфигурационные файлы приложения и возвращает объект ConfigParser."""
    with importlib.resources.path(resources, 'config.ini') as global_config:
        user_config = os.path.join(user_config_dir, 'config.ini')
        from_env = os.environ.get('TASK_DIARY_CONFIG', '')
        return make_config(global_config, user_config, from_env)


config = make_default_config()


def make_db_connection():
    """Возвращает объект подключения к БД."""
    sqlite3.register_converter(
        'DATE',
        lambda v: datetime.strptime(v.decode(), '%Y-%m-%d').date()
    )
    sqlite3.register_converter(
        'DATETIME',
        lambda v: datetime.strptime(v.decode(), '%Y-%m-%d %H-%M-%S')
    )
    
    db_name = os.path.join(
        user_data_dir, config.get('db', 'db_name')
    )
    
    conn = sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    
    return conn
