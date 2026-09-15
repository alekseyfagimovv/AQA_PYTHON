# src/routers/room
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.dependencies import get_async_session
from src.models.booking import RoomModel
from src.schemas.booking import RoomCreate, RoomResponse

router = APIRouter(prefix="/rooms", tags=["Rooms"])

@router.post("/", response_model=RoomResponse, status_code=status.HTTP_201_CREATED)
async def create_room(
    dto: RoomCreate, 
    db: Annotated[AsyncSession, Depends(get_async_session)]):
    new_room = RoomModel(**dto.model_dump())
    db.add(new_room)
    try:
        await db.commit()
        await db.refresh(new_room)
        return new_room
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Комната с таким именем уже существует"
        )
    
@router.get("/", response_model=list[RoomResponse])
async def get_rooms(db: Annotated[AsyncSession, Depends(get_async_session)]):
    query = select(RoomModel)
    result = await db.execute(query)
    return result.scalars().all()

@router.delete("/{room_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Удалить комнату")
async def del_rooms(room_id: int, db: Annotated[AsyncSession, Depends(get_async_session)]):
    query = select(RoomModel).filter_by(id=room_id)
    result = await db.execute(query)
    room = result.scalar_one_or_none()
    if room is None:
        raise HTTPException(
            status_code=404, 
            detail="Переговорная комната не найдена")
    await db.delete(room)
    await db.commit()

        
    