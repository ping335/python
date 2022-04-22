"""
name         - Имя пакета
version      - Версия пакета

description  - Краткое описание пакета
url          - URL-адрес пакета
license      - Лицензия
author       - Автор пакета
author_email - E-Mail автора пакета

packages     - Пакеты, которые нужно скопировать при установке
py_modules   - Модули, которые нужно скопировать при установке
scripts      - Запускаемые из консоли команды/скрипты

install_requires - Прямые зависимости, которые нужно установить
"""

from setuptools import setup


setup(
    name='task-diary',
    version='1.0.0',
    description='Console diary.',
    license='MIT',
    author='Kirill Vercetti',
    author_email='office@kyzima-spb.com',
    packages=['task_diary'],
    install_requires=[
        'appdirs>=1.4',
        'prettytable>=0.7',
    ]
)
