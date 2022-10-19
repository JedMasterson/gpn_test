from fastapi import FastAPI
import sqlalchemy
from datetime import datetime
import sqlite3
import csv

app = FastAPI()


@app.get()
def get_record_by_date():
    return
