# src\models\booking
from datetime import datetime
from typing import Annotated

from sqlalchemy import DateTime, ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

timestamp = Annotated[datetime, mapped_column(DateTime(timezone=True))]

class RoomModel(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))

    bookings: Mapped[list["BookingModel"]] = relationship(back_populates="room", cascade="all, delete-orphan")

class BookingModel(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id", ondelete="CASCADE"))

    title: Mapped[str] = mapped_column(String(150), nullable=False)
    employee_name: Mapped[str] = mapped_column(String(100), nullable=False)
    start_at: Mapped[datetime]
    end_at: Mapped[datetime]
    created_at: Mapped[timestamp] = mapped_column(
        server_default=text("TIMEZONE('utc', NOW())")
    )

    room: Mapped["RoomModel"] = relationship(back_populates="bookings")