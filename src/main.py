from fastapi import FastAPI
from src.auth.router import auth_router

app = FastAPI(title="PopcornBooking")

app.include_router(auth_router)
