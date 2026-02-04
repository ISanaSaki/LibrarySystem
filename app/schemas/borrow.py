from pydantic import BaseModel
from datetime import datetime


class BorrowResponse(BaseModel):
    id: int
    user_id: int
    book_id: int
    borrowed_at: datetime
    returned_at: datetime | None

    class Config:
        from_attributes = True