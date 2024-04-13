from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func


from src.database import Base


class Session(Base):
    __tablename__ = "session"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"))
    cinema_id: Mapped[int] = mapped_column(ForeignKey("cinema.id"))
    start_time: Mapped[datetime]

    movie: Mapped["Movie"] = relationship(back_populates="session")
    booking: Mapped["Booking"] = relationship(
        order_by="Booking.id", back_populates="session"
    )
