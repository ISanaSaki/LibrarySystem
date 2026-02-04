from fastapi import HTTPException, status
from app.models.user import User
from app.models.book import Book


def require_author(user: User):
    if user.role not in ("author", "admin"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only authors can perform this action"
        )


def require_book_owner(user: User, book: Book):
    if user.role == "admin":
        return

    if book.author.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not the owner of this book"
        )