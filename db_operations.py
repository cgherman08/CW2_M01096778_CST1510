import pandas as pd
import sqlite3
from app.db import conn



def migrate_it_tickets(conn):
    data1 = pd.read_csv('DATA\\it_tickets.csv')
    data1.to_sql('it_tickets', conn, if_exists='append', index=False)
    print('Data loaded successfully')
 
def migrate_datasets_metadata(conn):
    df = pd.read_csv('DATA\\datasets_metadata.csv')
    print(df.head())
    df.to_sql('datasets_metadata', conn, if_exists='append', index=False)
    print('Data loaded successfully') 


migrate_datasets_metadata(conn)