from databases import Database
from os import environ

DB_USER = environ.get('DB_USER', 'user')
DB_PASSWORD = environ.get('DB_PASSWORD', 'password')
DB_HOST = environ.get('DB_HOST', 'localhost')
DB_NAME = environ.get('DB_NAME', 'localhost')
DATABASE_URL = f'sqlite:///./database.db'

database = Database(DATABASE_URL)
