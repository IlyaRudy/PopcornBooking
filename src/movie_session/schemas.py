from datetime import datetime
from pydantic import BaseModel

from src.cinema.schemas import CinemaRead
from src.movie.schemas import MovieRead


class MovieSessionBase(BaseModel):
    start_time: datetime


class MovieSessionCreate(MovieSessionBase):
    movie_id: int
    cinema_id: int


class MovieSessionRead(MovieSessionBase):
    id: int
    movie: MovieRead
    cinema: CinemaRead
    # bookings: list[dict]

    class Config:
        from_attributes = True


class MovieSessionUpdate(BaseModel):
    movie_id: int | None = None
    cinema_id: int | None = None
    start_time: datetime | None = None
