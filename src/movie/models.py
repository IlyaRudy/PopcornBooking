from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func

from src.database import Base

if TYPE_CHECKING:
    from src.movie_session.models import MovieSession


class Movie(Base):
    __tablename__ = "movie"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str]
    description: Mapped[str]
    duration: Mapped[int]

    movie_session: Mapped["MovieSession"] = relationship(
        order_by="movie_session.c.id",
        back_populates="movie",
    )

    def __str__(self):
        return f"Movie: {self.title}"
