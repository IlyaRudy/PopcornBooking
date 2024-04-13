from datetime import datetime
from pydantic import BaseModel

from src.book.models import Booking
from src.movie.models import Movie


class SessionBase(BaseModel):
    movie_id: int
    cinema_id: int
    start_time: datetime


class SessionCreate(SessionBase):
    pass


class SessionRead(SessionBase):
    id: int
    movie: Movie
    bookings: list[Booking]

    class Config:
        orm_mode = True


class SessionUpdate(BaseModel):
    movie_id: int | None = None
    cinema_id: int | None = None
    start_time: datetime | None = None
