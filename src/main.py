from fastapi import FastAPI
from src.auth.router import auth_router
from src.cinema.router import cinema_router
from src.movie.router import movie_router
from src.movie_session.router import movie_session_router

app = FastAPI(title="PopcornBooking")

app.include_router(auth_router)
app.include_router(cinema_router)
app.include_router(movie_router)
app.include_router(movie_session_router)
