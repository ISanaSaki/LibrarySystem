from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BookCreate(BaseModel):
    title: str
    description: Optional[str] = None


class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_available: Optional[bool] = None


class BookOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    is_available: bool
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True