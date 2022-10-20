from fastapi import FastAPI
from routers import ping
import sqlalchemy
from datetime import datetime
import sqlite3
import requests
import csv

app = FastAPI()
app.include_router(ping.router)


@app.get('/get_record_date')
def get_record_by_date():
    return
