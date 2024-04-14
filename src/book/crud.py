from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.book.models import Booking
from sqlalchemy.orm import joinedload
from src.book.schemas import BookingCreate, BookingUpdate
from src.movie_session.models import MovieSession


async def get_booking(session: AsyncSession, booking_id: int):
    result = await session.execute(
        select(Booking)
        .options(
            joinedload(Booking.user),
            joinedload(Booking.movie_session).joinedload(MovieSession.movie),
            joinedload(Booking.movie_session).joinedload(MovieSession.cinema),
        )
        .filter(Booking.id == booking_id)
    )
    return result.scalars().first()


async def get_bookings(session: AsyncSession, skip: int = 0, limit: int = 100):
    result = await session.execute(
        select(Booking)
        .options(
            joinedload(Booking.user),
            joinedload(Booking.movie_session).joinedload(MovieSession.movie),
            joinedload(Booking.movie_session).joinedload(MovieSession.cinema),
        )
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()


async def create_booking(session: AsyncSession, booking: BookingCreate):
    db_booking = Booking(**booking.model_dump())
    session.add(db_booking)
    await session.commit()
    await session.refresh(db_booking)
    return db_booking


async def update_booking(db: AsyncSession, booking_id: int, booking: BookingUpdate):
    result = await db.execute(select(Booking).filter(Booking.id == booking_id))
    db_booking = result.scalars().first()
    if db_booking:
        update_data = booking.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_booking, key, value)
        await db.commit()
        await db.refresh(db_booking)
    return db_booking


async def delete_booking(db: AsyncSession, booking_id: int):
    result = await db.execute(select(Booking).filter(Booking.id == booking_id))
    db_booking = result.scalars().first()
    if db_booking:
        await db.delete(db_booking)
        await db.commit()
    return db_booking
