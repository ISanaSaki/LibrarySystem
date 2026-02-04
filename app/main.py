from fastapi import FastAPI
from app.api.router import api_router
from app.db.base import Base
from app.db.session import engine
from app.models import user, book,author,borrow

app = FastAPI(title="Library System")
app.include_router(api_router,prefix="/api")