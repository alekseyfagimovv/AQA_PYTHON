# src/routers/booking
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.dependencies import get_async_session
from src.models.booking import BookingModel, RoomModel
from src.schemas.booking import BookingCreate, BookingResponse

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(
    dto: BookingCreate, 
    db: Annotated[AsyncSession, Depends(get_async_session)]
):
    query = select(RoomModel).filter_by(id=dto.room_id)
    result = await db.execute(query)
    room = result.scalar_one_or_none()
    if room is None:
        raise HTTPException(
            status_code=404, 
            detail="Переговорная комната не найдена")
    overlap_query = select(BookingModel).filter(
    BookingModel.room_id == dto.room_id,
    BookingModel.start_at < dto.end_at,
    BookingModel.end_at > dto.start_at
    )
    overlap_result = await db.execute(overlap_query)
    existing_booking = overlap_result.scalar_one_or_none()
    if existing_booking is not None:
        raise HTTPException(status_code=409, detail="Данный временной слот в этой переговорной уже занят")
    new_booking = BookingModel(**dto.model_dump())
    db.add(new_booking)
    await db.commit()
    await db.refresh(new_booking)
    return new_booking

@router.get("/", response_model=list[BookingResponse])
async def get_bookings(db: Annotated[AsyncSession, Depends(get_async_session)]):
    query =  select(BookingModel)
    result = await db.execute(query)
    return result.scalars().all()

@router.get("/room/{room_id}", response_model=list[BookingResponse])
async def get_room_bookings(room_id: int, db: Annotated[AsyncSession, Depends(get_async_session)]):
    query = select(RoomModel).filter_by(id=room_id)
    start_query = await db.execute(query)
    room = start_query.scalar_one_or_none()
    if room is None:
        raise HTTPException(
            status_code=404, 
            detail="Переговорная комната не найдена")
    second_query = select(BookingModel).filter_by(room_id=room_id)
    result = await db.execute(second_query)
    return result.scalars().all()