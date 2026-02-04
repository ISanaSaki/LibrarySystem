from pydantic import BaseModel


class AuthorCreate(BaseModel):
    bio: str | None = None


class AuthorResponse(BaseModel):
    id: int
    user_id: int
    bio: str | None

    class Config:
        from_attributes = True