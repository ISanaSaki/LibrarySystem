from pydantic import BaseModel
from datetime import datetime


class BorrowedBookReport(BaseModel):
    book_id: int
    title: str
    borrowed_at: datetime
    returned_at: datetime | None

    class Config:
        from_attributes = True


class BookStatusCount(BaseModel):
    available: int
    unavailable: int