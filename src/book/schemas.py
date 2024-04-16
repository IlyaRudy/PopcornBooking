from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

from src.auth.schemas import UserRead
from src.movie_session.schemas import MovieSessionRead


class BookingBase(BaseModel):
    booked_seats: int
    booking_time: datetime
    status: str


class BookingCreate(BookingBase):
    user_id: UUID
    movie_session_id: int


class BookingRead(BookingBase):
    id: int
    user: UserRead
    movie_session: MovieSessionRead

    class Config:
        from_attributes = True


class BookingUpdate(BaseModel):
    user_id: int | None = None
    movie_session_id: int | None = None
    booked_seats: int | None = None
    booking_time: datetime | None = None
    status: str | None = None
