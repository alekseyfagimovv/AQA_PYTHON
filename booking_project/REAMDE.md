# Room Booking API

Сервис бронирования переговорок и песочница для обучения

## Стек
- FastAPI, SQLAlchemy (async), PostgreSQL
- Alembic, Docker, Pytest

## Запуск
docker compose up --build --detach

## Эндпоинты
- POST /auth/register
- POST /auth/login
- GET /rooms
- POST /bookings