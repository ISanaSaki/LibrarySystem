from sqlalchemy.orm import Session
from app.models.author import Author


def create_author(db: Session, user_id: int, bio: str | None = None):
    author = Author(user_id=user_id, bio=bio)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


def get_author_by_user_id(db: Session, user_id: int):
    return db.query(Author).filter(Author.user_id == user_id).first()


def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()