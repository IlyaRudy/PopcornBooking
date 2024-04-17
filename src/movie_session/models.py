from typing import TYPE_CHECKING

from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


if TYPE_CHECKING:
    from src.book.models import Booking
    from src.cinema.models import Cinema
    from src.movie.models import Movie


class MovieSession(Base):
    __tablename__ = "movie_session"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"))
    cinema_id: Mapped[int] = mapped_column(ForeignKey("cinema.id"))
    start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    movie: Mapped["Movie"] = relationship(back_populates="movie_session")
    cinema: Mapped["Cinema"] = relationship(back_populates="movie_session")
    bookings: Mapped[list["Booking"]] = relationship(back_populates="movie_session")
