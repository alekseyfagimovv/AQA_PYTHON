from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.booking import router as booking_router
from src.routers.room import router as room_router

app = FastAPI(title="Booking API")

origins = [
    "http://localhost",
    "http:192.168.0.103"
]

app.add_middleware(  
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(booking_router)  
app.include_router(room_router) 
