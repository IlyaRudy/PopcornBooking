from datetime import datetime
from pydantic import BaseModel

from src.auth.schemas import UserRead
from src.movie_session.models import MovieSession


class BookingBase(BaseModel):
    user_id: int
    session_id: int
    booked_seats: int
    booking_time: datetime
    status: str


class BookingCreate(BookingBase):
    pass


class BookingRead(BookingBase):
    id: int
    user: UserRead
    # movie_session: MovieSession

    class Config:
        from_attributes = True


class BookingUpdate(BaseModel):
    user_id: int | None = None
    session_id: int | None = None
    booked_seats: int | None = None
    booking_time: datetime | None = None
    status: str | None = None
