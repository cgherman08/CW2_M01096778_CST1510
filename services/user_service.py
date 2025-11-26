from app.db import conn
from app.users import add_user
import pandas as pd

def migrate_users():
    with open('DATA\\users.txt', 'r') as f:
        users = f.readlines()
        for user in users:
            name, hash = user.strip().split(',')
            add_user(conn, name, hash)
        conn.close()
        
def migrate_cyber_incidents(conn):
    data1 = pd.read_csv('DATA\\cyber_incidents.csv')
    data1.to_sql('cyber_incidents', conn, if_exists='append', index=False)
    print('Data load')

def migrate_it_tickets(conn):
    data1 = pd.read_csv('DATA\\it_tickets.csv')
    data1.to_sql('it_tickets', conn, if_exists='append', index=False)
    print('Data load')
 