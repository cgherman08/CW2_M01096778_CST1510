import pandas as pd
from database.db import get_connection



class DatabaseManager:
    """Handles SQLite database connections and queries."""
  
    def __init__(self, conn=None):
        self._conn = None
        
        if self._conn is None:
            self._conn = get_connection()
        
    
    def connect(self) -> None:
        if self._conn is None:
            self._conn = get_connection()
    
    def close(self) -> None:
        if self._conn is not None:
            self._conn.close()
            self._conn = None
    
    def set_user(self, name, hash):
        curr = self._conn.cursor()
        sql = """INSERT INTO users (user_name, password_hash) VALUES (?,?)"""
        param = (name, hash)
        curr.execute(sql, param)
        self._conn.commit()
        
    def get_all_users(self):
        curr = self._conn.cursor()
        sql = """SELECT * FROM users"""
        curr.execute(sql)
        all_users = curr.fetchall()
        return all_users
    
    def get_one_user(self, name):
        curr = self._conn.cursor()
        sql = """SELECT * FROM users WHERE user_name = ?"""
        param = (name,)
        curr.execute(sql, param)
        user = curr.fetchone()
        return(user)
    
    def update_user(self, old_name, new_name):
        curr = self._conn.cursor()
        sql = """UPDATE users SET user_name = ? WHERE user_name = ?"""
        param = (new_name, old_name)
        curr.execute(sql, param)
        self._conn.commit()
        
    def delete_user(self, name):
        curr = self._conn.cursor()
        sql = """DELETE FROM users  WHERE user_name = ?"""
        param = (name,)
        curr.execute(sql, param)
        self._conn.commit()
    
    
    def create_user_table(self):
        curr = self._conn.cursor()
        curr.execute(
            """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL)
                """)
        self._conn.commit()
        print('User table created!')

    def get_all_cyber_incidents(self):
        sql = 'SELECT * from cyber_incidents'
        data = pd.read_sql(sql, self._conn)
        return data
    
    def load_datasets(self):
        sql = """
        SELECT * from datasets_metadata
        """
        return pd.read_sql(sql, self._conn)
    
    def load_tickets(self):
        df = pd.read_sql('SELECT * FROM it_tickets', self._conn)
        self._conn.close()
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
        return df

class DBMigrator:
    def __init__(self, conn=None):
        if conn is None:
            self._conn = get_connection()
        else:
            self._conn = conn
            
    def migrate_it_tickets(self):
        data1 = pd.read_csv('DATA\\it_tickets.csv')
        data1.to_sql('it_tickets', self.conn, if_exists='append', index=False)
        print('IT Tickets data loaded successfully')

    def migrate_datasets_metadata(self):
        df = pd.read_csv('DATA\\datasets_metadata.csv')
        df.to_sql('datasets_metadata', self.conn, if_exists='append', index=False)
        print('Datasets metadata loaded successfully')
        
    def migrate_cyber_incidents(self):
        data2 = pd.read_csv('DATA\\cyber_incidents.csv')
        data2.to_sql('cyber_incidents', self.conn, if_exists='append', index=False)
        print('Cyber Incidents data loaded successfully')
        
    def migrate_users(self):
        with open('DATA\\users.txt', 'r') as f:
            users = f.readlines()
            for user in users:
                name, hash = user.strip().split(',')
                DatabaseManager().set_user(name, hash)
            DatabaseManager().close()
            