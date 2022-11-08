import datetime
from typing import Optional

import sqlalchemy
from sqlalchemy import and_

from src.app.db import database
from src.app.models.records import records_table

date_format = '%Y-%m-%d'


async def get_record_up_to_date(date):
    record_date = records_table.c.Date
    request_date = datetime.datetime.strptime(date, date_format)
    query = sqlalchemy.select([records_table]).where(record_date <= request_date)
    select_res = database.execute(query)
    return select_res.fetchall()


async def get_record_from_date(date):
    record_date = records_table.c.Date
    request_date = datetime.datetime.strptime(date, date_format)
    query = sqlalchemy.select([records_table]).where(record_date >= request_date)
    select_res = database.execute(query)
    return select_res.fetchall()


async def get_record_between_dates(first_date, second_date):
    record_date = records_table.c.Date
    request_frst_date = datetime.datetime.strptime(first_date, date_format)
    request_scnd_date = datetime.datetime.strptime(second_date, date_format)
    query = sqlalchemy.select([records_table]).where(and_(
        request_frst_date <= record_date,
        record_date <= request_scnd_date))
    select_res = database.execute(query)
    return select_res.fetchall()
