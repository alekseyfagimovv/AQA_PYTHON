from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.booking import router as booking_router #Это зачем 
from src.routers.room import router as room_router #Это зачем 

app = FastAPI(title="Booking API")

origins = [
    "https://frontend"
]

app.add_middleware( # этот инструмент вообще подробно полностью разобрать бы
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(booking_router) #Это зачем
app.include_router(room_router)#Это зачем
