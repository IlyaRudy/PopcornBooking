from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.cinema.models import Cinema
from src.cinema.schemas import CinemaCreate, CinemaUpdate, CinemaRead


async def get_cinema(session: AsyncSession, cinema_id: int):
    result = await session.execute(select(Cinema).filter(Cinema.id == cinema_id))
    return result.scalars().first()


async def get_cinemas(session: AsyncSession, skip: int = 0, limit: int = 100):
    result = await session.execute(select(Cinema).offset(skip).limit(limit))
    return result.scalars().all()


async def create_cinema(session: AsyncSession, cinema: CinemaCreate):
    db_cinema = Cinema(**cinema.model_dump())
    session.add(db_cinema)
    await session.commit()
    await session.refresh(db_cinema)
    return db_cinema


async def update_cinema(db: AsyncSession, cinema_id: int, cinema: CinemaUpdate):
    result = await db.execute(select(Cinema).filter(Cinema.id == cinema_id))
    db_cinema = result.scalars().first()
    if db_cinema:
        update_data = cinema.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_cinema, key, value)
        await db.commit()
        await db.refresh(db_cinema)
    return db_cinema


async def delete_cinema(db: AsyncSession, cinema_id: int):
    result = await db.execute(select(Cinema).filter(Cinema.id == cinema_id))
    db_cinema = result.scalars().first()
    if db_cinema:
        await db.delete(db_cinema)
        await db.commit()
    return db_cinema
