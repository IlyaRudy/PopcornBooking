from datetime import datetime
from pydantic import BaseModel

from src.auth.models import User
from src.session.models import Session


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
    user: User
    session: Session

    class Config:
        orm_mode = True


class BookingUpdate(BaseModel):
    user_id: int | None = None
    session_id: int | None = None
    booked_seats: int | None = None
    booking_time: datetime | None = None
    status: str | None = None
