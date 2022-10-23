import sqlite3
import pandas as pd
from pathlib import Path

Path('database.db').touch()

connection = sqlite3.connect(database='database.db')

db_cursor = connection.cursor()

db_cursor.execute('''create table records
(
    "id"          integer
        constraint table_name_pk
            primary key,
    "Date"      str,
    "Open"      float,
    "High"      float,
    "Low"       float,
    "Close"     float,
    "Adj Close" float,
    "Volume"    integer
)''')

records = pd.read_csv("/home/jedmasterson/Documents/Projects/GPN_test/data/aapl.csv")
records.to_sql('records', connection, if_exists='append', index=False)
