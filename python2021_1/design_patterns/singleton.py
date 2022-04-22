"""
Singleton (Одиночка)
Порождающий

Гарантирует, что у класса есть только один экземпляр,
и предоставляет к нему глобальную точку доступа.
"""

from configparser import ConfigParser
import copy


class SingletonMeta(type):
    __instances = {}
    
    def __init__(cls, name, bases, d):
        super().__init__(name, bases, d)
        cls.__deepcopy__ = cls.__copy__
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]
    
    def __copy__(cls, *args, **kwargs):
        raise TypeError("You can't have more then one instance.")


class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.config = ConfigParser()
    
    def __getattr__(self, name):
        if name.startswith('__'):
            return super().__getattr__(name)
        return getattr(self.config, name)


def make_db_connection():
    config = Config()
    print(config.get('main', 'db_host'))


def load_config():
    config = Config()
    config.add_section('main')
    config.set('main', 'db_host', 'localhost')


load_config()
make_db_connection()

# config = Config()
# config_copy = copy.copy(config)
# print(config is config_copy)
# config_copy = copy.deepcopy(config)
# print(config is config_copy)
