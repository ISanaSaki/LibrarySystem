from sqlalchemy.orm import Session
from typing import Optional

from app.models.book import Book
from app.models.author import Author
from app.schemas.book import BookCreate, BookUpdate
from fastapi import HTTPException, status


def create_book(db: Session, book: BookCreate, author_id: int):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Author not found"
    )
    db_book = Book(
        title=book.title,
        description=book.description,
        author_id=author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(
    db: Session,
    author_id: Optional[int] = None,
    is_available: Optional[bool] = None
):
    query = db.query(Book)

    if author_id is not None:
        query = query.filter(Book.author_id == author_id)

    if is_available is not None:
        query = query.filter(Book.is_available == is_available)

    return query.all()


def get_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return book


def update_book(db: Session, book: Book, data: BookUpdate):
    for field, value in data.dict(exclude_unset=True).items():
        setattr(book, field, value)

    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book: Book):
    db.delete(book)
    db.commit()