from fastapi import FastAPI
from src.auth.router import auth_router
from src.book.router import book_router

app = FastAPI(title="PopcornBooking")

app.include_router(auth_router)
app.include_router(book_router)
