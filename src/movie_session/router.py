from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.movie_session import crud, schemas
from src.database import get_async_session

movie_session_router = APIRouter(prefix="/movie_session", tags=["Movie Session"])


@movie_session_router.post("/", response_model=schemas.MovieSessionCreate)
async def create_movie_session(
    movie_session: schemas.MovieSessionCreate,
    session: AsyncSession = Depends(get_async_session),
):
    return await crud.create_movie_session(session=session, movie_session=movie_session)


@movie_session_router.get("/", response_model=list[schemas.MovieSessionRead])
async def read_movie_sessions(
    skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_async_session)
):
    movie_sessions = await crud.get_movie_sessions(session, skip=skip, limit=limit)
    return movie_sessions


@movie_session_router.get(
    "/{movie_session_id}", response_model=schemas.MovieSessionRead
)
async def read_movie_session(
    movie_session_id: int, session: AsyncSession = Depends(get_async_session)
):
    db_session = await crud.get_movie_session(
        session, movie_session_id=movie_session_id
    )
    if db_session is None:
        raise HTTPException(
            status_code=404,
            detail=f"Movie sesssion with id={movie_session_id} not found",
        )
    return db_session


@movie_session_router.put(
    "/{movie_session_id}", response_model=schemas.MovieSessionUpdate
)
async def update_movie_session(
    movie_session_id: int,
    movie_session: schemas.MovieSessionUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    db_session = await crud.update_movie_session(
        session, movie_session_id, movie_session
    )
    if db_session is None:
        raise HTTPException(
            status_code=404,
            detail=f"Movie sesssion with id={movie_session_id} not found",
        )
    return db_session


@movie_session_router.delete("/{movie_session_id}")
async def delete_movie_session(
    movie_session_id: int, session: AsyncSession = Depends(get_async_session)
):
    db_session = await crud.delete_movie_session(session, movie_session_id)
    if db_session is None:
        raise HTTPException(
            status_code=404,
            detail=f"Movie sesssion with id={movie_session_id} not found",
        )
    return db_session
