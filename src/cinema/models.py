from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func

from src.database import Base


class Cinema(Base):
    __tablename__ = "cinema"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    city: Mapped[str | None]
    city_district: Mapped[str | None]
    address: Mapped[str | None]
