import sqlite3
from pathlib import Path

DATA_DIR = Path('DATA')
DATA_PATH = DATA_DIR / 'intelligence_platform.db'

def get_connection():
    conn = sqlite3.connect(DATA_PATH, check_same_thread=False)
    # conn = sqlite3.connect('DATA/intelligence_platform.db', check_same_thread=False)
    return conn 