from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func

from src.database import Base


class Movie(Base):
    __tablename__ = "movie"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str]
    description: Mapped[str]
    duration: Mapped[int]

    session: Mapped["Session"] = relationship(
        order_by="Session.id", back_populates="movie"
    )
