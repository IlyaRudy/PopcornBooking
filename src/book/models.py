from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func


from src.database import Base


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
