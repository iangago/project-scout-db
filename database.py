import sqlite3 as sql
import os

DB_NAME = "scout.db"

def get_connection():
    return sql.connect(DB_NAME)

def initialize_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    conn = get_connection()

    with open("schema.sql", "r") as f:
        schema = f.read()

    conn.executescript(schema)
    conn.commit()
    conn.close()