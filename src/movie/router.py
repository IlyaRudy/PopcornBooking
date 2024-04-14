from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.movie import crud, schemas
from src.database import get_async_session

movie_router = APIRouter(prefix="/movie", tags=["Movie"])


@movie_router.post("/", response_model=schemas.MovieRead)
async def create_movie(
    movie: schemas.MovieCreate, session: AsyncSession = Depends(get_async_session)
):
    return await crud.create_movie(session=session, movie=movie)


@movie_router.get("/", response_model=list[schemas.MovieRead])
async def read_movies(
    skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_async_session)
):
    movies = await crud.get_movies(session, skip=skip, limit=limit)
    return movies


@movie_router.get("/{movie_id}", response_model=schemas.MovieRead)
async def read_movie(movie_id: int, session: AsyncSession = Depends(get_async_session)):
    db_movie = await crud.get_movie(session, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(
            status_code=404, detail=f"Movie with id={movie_id} not found"
        )
    return db_movie


@movie_router.put("/{movie_id}", response_model=schemas.MovieUpdate)
async def update_movie(
    movie_id: int,
    movie: schemas.MovieUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    db_movie = await crud.update_movie(session, movie_id, movie)
    if db_movie is None:
        raise HTTPException(
            status_code=404, detail=f"Movie with id={movie_id} not found"
        )
    return db_movie


@movie_router.delete("/{movie_id}")
async def delete_movie(
    movie_id: int, session: AsyncSession = Depends(get_async_session)
):
    db_movie = await crud.delete_movie(session, movie_id)
    if db_movie is None:
        raise HTTPException(
            status_code=404, detail=f"Movie with id={movie_id} not found"
        )
    return db_movie
