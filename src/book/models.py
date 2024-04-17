from typing import TYPE_CHECKING

from datetime import datetime
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func


from src.database import Base


if TYPE_CHECKING:
    from src.auth.models import User
    from src.movie_session.models import MovieSession


class Booking(Base):
    __tablename__ = "booking"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    movie_session_id: Mapped[int] = mapped_column(
        ForeignKey("movie_session.id"), nullable=False
    )
    booked_seats: Mapped[int]
    booking_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    status: Mapped[str]

    user: Mapped["User"] = relationship(back_populates="bookings")
    movie_session: Mapped["MovieSession"] = relationship(back_populates="bookings")
