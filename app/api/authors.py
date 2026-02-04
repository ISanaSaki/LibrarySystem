from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.schemas.author import AuthorCreate, AuthorResponse
from app.crud.author import create_author, get_author_by_user_id

router = APIRouter()


@router.post("/", response_model=AuthorResponse)
def create_author_profile(
    author_data: AuthorCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    existing = get_author_by_user_id(db, current_user.id)
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Author profile already exists"
        )

    author = create_author(
        db=db,
        user_id=current_user.id,
        bio=author_data.bio
    )

    return author