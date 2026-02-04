from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.borrow import Borrow
from app.models.book import Book


def get_user_borrowed_books(db: Session, user_id: int):
    return (
        db.query(
            Book.id.label("book_id"),
            Book.title,
            Borrow.borrowed_at,
            Borrow.returned_at,
        )
        .join(Borrow, Borrow.book_id == Book.id)
        .filter(Borrow.user_id == user_id)
        .all()
    )


def get_currently_borrowed_books(db: Session):
    return (
        db.query(
            Book.id.label("book_id"),
            Book.title,
            Borrow.borrowed_at,
        )
        .join(Borrow, Borrow.book_id == Book.id)
        .filter(Borrow.returned_at.is_(None))
        .all()
    )


def get_author_books(db: Session, author_id: int):
    return db.query(Book).filter(Book.author_id == author_id).all()


def get_books_status_count(db: Session):
    available = db.query(func.count(Book.id)).filter(Book.is_available.is_(True)).scalar()
    unavailable = db.query(func.count(Book.id)).filter(Book.is_available.is_(False)).scalar()

    return {
        "available": available,
        "unavailable": unavailable,
    }