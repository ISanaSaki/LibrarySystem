from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.session import get_db
from app.models import Book, Borrow
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/my-borrows")
def my_borrowed_books(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    borrows = (
        db.query(Borrow)
        .filter(
            Borrow.user_id == current_user.id,
            Borrow.returned_at.is_(None)
        )
        .all()
    )

    return [
        {
            "book_id": b.book_id,
            "borrowed_at": b.borrowed_at
        }
        for b in borrows
    ]
@router.get("/my-books")
def my_written_books(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != "author":
        return {"detail": "Only authors can see this"}

    books = db.query(Book).filter(Book.author_id == current_user.id).all()

    return books
@router.get("/borrowed-books")
def borrowed_books(db: Session = Depends(get_db)):
    books = db.query(Book).filter(Book.is_available == False).all()
    return books
@router.get("/stats")
def books_stats(db: Session = Depends(get_db)):
    total = db.query(func.count(Book.id)).scalar()
    available = db.query(func.count(Book.id)).filter(Book.is_available == True).scalar()
    borrowed = total - available

    return {
        "total": total,
        "available": available,
        "borrowed": borrowed
    }