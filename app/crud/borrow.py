from sqlalchemy.orm import Session
from app.models.borrow import Borrow
from app.models.book import Book
from fastapi import HTTPException, status


def borrow_book(db: Session, user_id: int, book: Book):
    if not book.is_available:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book is not available"
        )

    borrow = Borrow(
        user_id=user_id,
        book_id=book.id
    )

    book.is_available = False

    db.add(borrow)
    db.commit()
    db.refresh(borrow)

    return borrow


def return_book(db: Session, user_id: int, book: Book):
    borrow = (
        db.query(Borrow)
        .filter(
            Borrow.book_id == book.id,
            Borrow.user_id == user_id,
            Borrow.returned_at.is_(None)
        )
        .first()
    )

    if not borrow:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have not borrowed this book"
        )

    borrow.returned_at = borrow.borrowed_at.now()
    book.is_available = True

    db.commit()
    db.refresh(borrow)

    return borrow