from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.book import crud, schemas
from src.database import get_async_session

booking_router = APIRouter(prefix="/booking", tags=["Booking"])


@booking_router.post("/", response_model=schemas.BookingCreate)
async def create_booking(
    booking: schemas.BookingCreate, session: AsyncSession = Depends(get_async_session)
):
    return await crud.create_booking(session=session, booking=booking)


@booking_router.get("/", response_model=list[schemas.BookingRead])
async def read_bookings(
    skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_async_session)
):
    bookings = await crud.get_bookings(session, skip=skip, limit=limit)
    return bookings


@booking_router.get("/{booking_id}", response_model=schemas.BookingRead)
async def read_booking(
    booking_id: int, session: AsyncSession = Depends(get_async_session)
):
    db_booking = await crud.get_booking(session, booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(
            status_code=404, detail=f"Booking with id={booking_id} not found"
        )
    return db_booking


@booking_router.put("/{booking_id}", response_model=schemas.BookingUpdate)
async def update_booking(
    booking_id: int,
    booking: schemas.BookingUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    db_booking = await crud.update_booking(session, booking_id, booking)
    if db_booking is None:
        raise HTTPException(
            status_code=404, detail=f"Booking with id={booking_id} not found"
        )
    return db_booking


@booking_router.delete("/{booking_id}")
async def delete_booking(
    booking_id: int, session: AsyncSession = Depends(get_async_session)
):
    db_booking = await crud.delete_booking(session, booking_id)
    if db_booking is None:
        raise HTTPException(
            status_code=404, detail=f"Booking with id={booking_id} not found"
        )
    return db_booking
