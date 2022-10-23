import datetime
from typing import Optional

from sqlalchemy import and_

from src.app.db import database
from src.app.models.records import records_table

date_format = '%Y-%m-%d'


async def get_record_up_to_date(date):
    record_date = records_table.c.Date
    request_date = datetime.datetime.strptime(date, date_format)
    query = records_table.select().where(record_date <= request_date)
    return await database.fetch_one(query)


async def get_record_from_date(date):
    record_date = records_table.c.Date
    request_date = datetime.datetime.strptime(date, date_format)
    query = records_table.select().where(record_date >= request_date)
    return await database.fetch_one(query)


async def get_record_between_dates(first_date, second_date):
    record_date = records_table.c.Date
    request_frst_date = datetime.datetime.strptime(first_date, date_format)
    request_scnd_date = datetime.datetime.strptime(second_date, date_format)
    query = records_table.select().where(and_(
        request_frst_date <= record_date,
        record_date <= request_scnd_date))
    return await database.fetch_one(query)
