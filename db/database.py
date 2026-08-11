import sqlite3 as sql
import os
import job as j

DB_NAME = "db/scout.db"

def get_connection():
    return sql.connect(DB_NAME)

def initialize_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    conn = get_connection()

    with open("db/schema.sql", "r") as f:
        schema = f.read()

    conn.executescript(schema)
    conn.commit()
    conn.close()

def fill_jobs(clean_data):
    conn = get_connection()

    for term in clean_data:
        for job in term[1]:
            j.insert_job(conn, job)

    conn.commit()
    conn.close()
