from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from src.app.schemas import records
from src.app.utils import records as records_utils

router = APIRouter()


@router.get('/get_record/{date}')
async def get_record_up_to(start_date: str | None = None, end_date: str | None = None):
    if start_date and end_date:
        db_record = await records_utils.get_record_between_dates(first_date=start_date, second_date=end_date)
        if not db_record:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Record not found')
        return db_record
    elif start_date:
        db_record = await records_utils.get_record_from_date(date=start_date)
        if not db_record:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Record not found')
        return db_record
    elif end_date:
        db_record = await records_utils.get_record_up_to_date(date=end_date)
        if not db_record:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Record not found')
        return db_record
