from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func

from src.auth.models import User
from src.database import Base


class Movie(Base):
    __tablename__ = "movie"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str]
    description: Mapped[str]
    duration: Mapped[int]


class Session(Base):
    __tablename__ = "session"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"))
    start_time: Mapped[datetime]
    room_number: Mapped[str]
    movie: Mapped["Movie"] = relationship(back_populates="session")


Movie.sessions = relationship("Session", order_by=Session.id, back_populates="movie")


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    session_id: Mapped[int] = mapped_column(ForeignKey("session.id"), nullable=False)
    booked_seats: Mapped[int]
    booking_time: Mapped[datetime] = mapped_column(server_default=func.now())
    status: Mapped[str]

    user: Mapped["User"] = relationship(back_populates="booking")
    session: Mapped["Session"] = relationship(back_populates="booking")


User.bookings = relationship("Booking", order_by=Booking.id, back_populates="user")
Session.bookings = relationship(
    "Booking", order_by=Booking.id, back_populates="session"
)
