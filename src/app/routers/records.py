from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from src.app.schemas import records
from src.app.utils import records as records_utils

router = APIRouter()


@router.get('/get_record_up_to/{date}')
async def get_record_up_to(date: str):
    db_record = await records_utils.get_record_up_to_date(date=date)
    if not db_record:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Record not found')


@router.get('/get_record_from/{date}')
async def get_record_from(date: str):
    db_record = await records_utils.get_record_from_date(date=date)
    if not db_record:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Record not found')


@router.get('/get_record_between/{first}and{second}')
async def get_record_between(first: str, second: str):
    db_record = await records_utils.get_record_between_dates(first_date=first, second_date=second)
    if not db_record:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Record not found')
