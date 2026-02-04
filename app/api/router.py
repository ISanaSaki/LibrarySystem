from fastapi import APIRouter
from app.api import auth, books,authors,borrow,reports

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(books.router, prefix="/books", tags=["Books"])
api_router.include_router(authors.router, prefix="/authors", tags=["Authors"]) 
api_router.include_router(borrow.router, prefix="/borrow", tags=["Borrow"]) 
api_router.include_router(reports.router, prefix="/reports", tags=["Reports"]) 