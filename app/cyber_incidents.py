import pandas as pd
from .db import get_connection

conn = get_connection()

def get_all_cyber_incidents(conn):
    sql = 'SELECT * from cyber_incidents'
    data = pd.read_sql(sql, conn)
    return data

def migrate_cyber_incidents(conn):
    data1 = pd.read_csv('DATA\\cyber_incidents.csv')
    data1.to_sql('cyber_incidents', conn, if_exists='append', index=False)
    print('Data load successfully')
    