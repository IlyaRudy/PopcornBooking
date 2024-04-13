from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.cinema import crud, schemas
from src.database import get_async_session

cinema_router = APIRouter(prefix="/cinema", tags=["Cinema"])


@cinema_router.post("/", response_model=schemas.CinemaRead)
async def create_cinema(
    cinema: schemas.CinemaCreate, session: AsyncSession = Depends(get_async_session)
):
    return await crud.create_cinema(session=session, cinema=cinema)


@cinema_router.get("/", response_model=list[schemas.CinemaRead])
async def read_cinemas(
    skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_async_session)
):
    cinemas = await crud.get_cinemas(session, skip=skip, limit=limit)
    return cinemas


@cinema_router.get("/{cinema_id}", response_model=schemas.CinemaRead)
async def read_cinema(
    cinema_id: int, session: AsyncSession = Depends(get_async_session)
):
    db_cinema = await crud.get_cinema(session, cinema_id=cinema_id)
    if db_cinema is None:
        raise HTTPException(
            status_code=404, detail=f"Cinema with id={cinema_id} not found"
        )
    return db_cinema


@cinema_router.put("/{cinema_id}", response_model=schemas.CinemaUpdate)
async def update_cinema(
    cinema_id: int,
    cinema: schemas.CinemaUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    db_cinema = await crud.update_cinema(session, cinema_id, cinema)
    if db_cinema is None:
        raise HTTPException(
            status_code=404, detail=f"Cinema with id={cinema_id} not found"
        )
    return db_cinema


@cinema_router.delete("/{cinema_id}")
async def delete_cinema(
    cinema_id: int, session: AsyncSession = Depends(get_async_session)
):
    db_cinema = await crud.delete_cinema(session, cinema_id)
    if db_cinema is None:
        raise HTTPException(
            status_code=404, detail=f"Cinema with id={cinema_id} not found"
        )
    return db_cinema
