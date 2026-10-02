# src\schemas\booking
from datetime import datetime

from pydantic import BaseModel, Field, field_validator, model_validator


class RoomCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)

class RoomResponse(BaseModel):
    id: int
    name: str
    description: str | None = None

    model_config = {
                "from_attributes": True
            }
    
class BookingCreate(BaseModel):
    room_id: int = Field(gt=0)
    title: str 
    employee_name: str 
    start_at: datetime
    end_at: datetime

    @field_validator('title', 'employee_name', mode='before')
    @classmethod
    def clean_whitespace(cls, v: str) -> str:
        return v.strip()

    @model_validator(mode='after')
    def time_range(self) -> str | None:
        if self.end_at < self.start_at:
            raise ValueError('Дата/время `end_at` должны быть строго позже, чем `start_at')
        return self

    
class BookingResponse(BaseModel):
    id: int 
    room_id: int 
    title: str 
    employee_name: str 
    start_at: datetime
    end_at: datetime
    
    created_at: datetime 

    model_config = {
                "from_attributes": True
            }