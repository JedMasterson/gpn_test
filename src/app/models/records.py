import sqlite3

import sqlalchemy
import datetime
import sqlalchemy.dialects.sqlite

metadata = sqlalchemy.MetaData()

records_table = sqlalchemy.Table(
    'records',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('Date', sqlalchemy.DateTime),
    sqlalchemy.Column('Open', sqlalchemy.Float),
    sqlalchemy.Column('High', sqlalchemy.Float),
    sqlalchemy.Column('Low', sqlalchemy.Float),
    sqlalchemy.Column('Close', sqlalchemy.Float),
    sqlalchemy.Column('Adj Close', sqlalchemy.Float),
    sqlalchemy.Column('Volume', sqlalchemy.Integer),
)
