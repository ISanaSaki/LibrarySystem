from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.book import Book
from app.schemas.borrow import BorrowResponse
from app.crud.borrow import borrow_book, return_book

router = APIRouter()


@router.post("/borrow/{book_id}", response_model=BorrowResponse)
def borrow_book_api(
    book_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return borrow_book(db, current_user.id, book)


@router.post("/return/{book_id}", response_model=BorrowResponse)
def return_book_api(
    book_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return return_book(db, current_user.id, book)