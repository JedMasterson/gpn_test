from pydantic import BaseModel


class RecordCreate(BaseModel):
    id: int
    date: str
    open: float
    high: float
    low: float
    close: float
    adj_close: float
    volume: int
