from fastapi import FastAPI
from src.auth.router import auth_router
from src.cinema.router import cinema_router
from src.movie.router import movie_router

app = FastAPI(title="PopcornBooking")

app.include_router(auth_router)
app.include_router(cinema_router)
app.include_router(movie_router)
