import sqlite3
import os.path
from flask import g


def connect():
    status = 0
    try:
        file_database = os.path.abspath('app/bases/principal.db')
        g.db = sqlite3.connect(file_database)
    except:
        status = 1
    return status


def select(sql):
    c = g.db.cursor()
    c.execute(sql)
    sort_data = c.fetchone()
    return sort_data


def insert(table, fields, values):
    fsql = f'INSERT INTO {table} ({",".join(fields)}) VALUES ({(("?" + ",") * len(fields))[:-1]})'
    dbc = g.db.cursor()
    dbc.execute(fsql, values)
    g.db.commit()