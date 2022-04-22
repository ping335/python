"""
SQLite3

:memory: - БД в оперативной памяти

DDL (Data Definition Language)
    CREATE TABLE
DML (Data Manipulation Language)
    INSERT INTO
    UPDATE
    DELETE
    SELECT
"""

from datetime import datetime
import sqlite3


# conn = sqlite3.connect('diary.sqlite3')
# 
# try:
#     sql = '''
#     CREATE TABLE IF NOT EXISTS task (
#         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#         title VARCHAR(100) NOT NULL,
#         planned TIMESTAMP NOT NULL,
#         description TEXT NOT NULL DEFAULT '',
#         done BOOLEAN NOT NULL DEFAULT 0,
#         created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
#     )
#     '''
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
# finally:
#     conn.close()


with sqlite3.connect('diary.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    conn.row_factory = sqlite3.Row
    
    sql = '''
    CREATE TABLE IF NOT EXISTS task (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        title VARCHAR(100) NOT NULL,
        planned TIMESTAMP NOT NULL,
        description TEXT NOT NULL DEFAULT '',
        done BOOLEAN NOT NULL DEFAULT 0,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    '''
    conn.execute(sql)
    
    sql = '''
        INSERT INTO task (title, planned, description) VALUES (?, ?, ?)
    '''
    conn.execute(
        sql,
        ('Сходить за продуктами', datetime(2021, 2, 20, 16), 'Список продуктов...')
    )
    
    sql = '''
        SELECT
            id, title, planned, description, done, created
        FROM
            task
    '''
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    
    for task in rows:
        print(type(task[0]), type(task[2]), ' / ', task['id'], task['planned'])
    
"""
UPDATE task SET title=?, planned=?, description=? WHERE id=?
DELETE FROM task WHERE id=?
"""

    
    
