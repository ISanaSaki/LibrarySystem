from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.session import get_db
from app.schemas.book import BookCreate, BookUpdate, BookOut
from app.crud import book as crud_book
from app.core.dependencies import get_current_user
from app.models.user import User
from app.utils.permissions import require_author, require_book_owner

router = APIRouter()


@router.post("/", response_model=BookOut)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    author = require_author(current_user)
    return crud_book.create_book(db=db, book=book, author_id=current_user.id)

@router.get("/", response_model=List[BookOut])
def list_books(
    author_id: Optional[int] = None,
    is_available: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    return crud_book.get_books(db, author_id, is_available)


@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud_book.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{book_id}", response_model=BookOut)
def update_book(
    book_id: int,
    data: BookUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    book = crud_book.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    require_book_owner(current_user, book)
    return crud_book.update_book(db, book, data)


@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    book = crud_book.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    require_book_owner(current_user, book)
    crud_book.delete_book(db, book)
    return {"detail": "Book deleted"}