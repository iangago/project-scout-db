from database import get_connection

def seed_database():
    conn = get_connection()

    with open("seed.sql", "r") as f:
            seed = f.read()

    conn.executescript(seed)
    conn.commit()
    conn.close()