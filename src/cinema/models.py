from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func

from src.database import Base

if TYPE_CHECKING:
    from src.movie_session.models import MovieSession


class Cinema(Base):
    __tablename__ = "cinema"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    city: Mapped[str | None]
    city_district: Mapped[str | None]
    address: Mapped[str | None]

    movie_session: Mapped["MovieSession"] = relationship(back_populates="cinema")

    def __str__(self):
        return f"Cinema: {self.name} - city: {self.city}"
