from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.movie.models import Movie
from src.movie.schemas import MovieCreate, MovieRead, MovieUpdate


async def get_movie(session: AsyncSession, movie_id: int):
    result = await session.execute(select(Movie).filter(Movie.id == movie_id))
    return result.scalars().first()


async def get_movies(session: AsyncSession, skip: int = 0, limit: int = 100):
    result = await session.execute(select(Movie).offset(skip).limit(limit))
    return result.scalars().all()


async def create_movie(session: AsyncSession, movie: MovieCreate):
    db_movie = Movie(**movie.model_dump())
    session.add(db_movie)
    await session.commit()
    await session.refresh(db_movie)
    return db_movie


async def update_movie(db: AsyncSession, movie_id: int, movie: MovieUpdate):
    result = await db.execute(select(Movie).filter(Movie.id == movie_id))
    db_movie = result.scalars().first()
    if db_movie:
        update_data = movie.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_movie, key, value)
        await db.commit()
        await db.refresh(db_movie)
    return db_movie


async def delete_movie(db: AsyncSession, movie_id: int):
    result = await db.execute(select(Movie).filter(Movie.id == movie_id))
    db_movie = result.scalars().first()
    if db_movie:
        await db.delete(db_movie)
        await db.commit()
    return db_movie
