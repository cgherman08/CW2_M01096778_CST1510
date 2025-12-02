from db import conn

def create_user_table():
    curr = conn.cursor()
    curr.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL)
            """)
    conn.commit()
    print('User table created!')


