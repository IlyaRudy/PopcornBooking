from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload, selectinload
from src.movie_session.models import MovieSession
from src.movie_session.schemas import (
    MovieSessionCreate,
    MovieSessionUpdate,
)


async def get_movie_session(session: AsyncSession, movie_session_id: int):
    result = await session.execute(
        select(MovieSession)
        .options(joinedload(MovieSession.movie), selectinload(MovieSession.cinema))
        .filter(MovieSession.id == movie_session_id)
    )
    return result.scalars().first()


async def get_movie_sessions(session: AsyncSession, skip: int = 0, limit: int = 100):
    result = await session.execute(
        select(MovieSession)
        .options(joinedload(MovieSession.movie), selectinload(MovieSession.cinema))
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()


async def create_movie_session(
    session: AsyncSession, movie_session: MovieSessionCreate
):
    db_session = MovieSession(**movie_session.model_dump())
    session.add(db_session)
    await session.commit()
    await session.refresh(db_session)
    return db_session


async def update_movie_session(
    session: AsyncSession, movie_session_id: int, movie_session: MovieSessionUpdate
):
    result = await session.execute(
        select(MovieSession).filter(MovieSession.id == movie_session_id)
    )
    db_session = result.scalars().first()
    if db_session:
        update_data = movie_session.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_session, key, value)
        await session.commit()
        await session.refresh(db_session)
    return db_session


async def delete_movie_session(session: AsyncSession, movie_session_id: int):
    result = await session.execute(
        select(MovieSession).filter(MovieSession.id == movie_session_id)
    )
    db_session = result.scalars().first()
    if db_session:
        await session.delete(db_session)
        await session.commit()
    return db_session
