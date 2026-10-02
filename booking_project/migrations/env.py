import asyncio
import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config

# Импортируем вашу базовую модель для поддержки автогенерации (--autogenerate)
from src.models import Base

# Объект конфигурации Alembic, предоставляющий доступ к значениям из alembic.ini
config = context.config

# Динамически собираем URL подключения из переменных окружения Docker-контейнера.
# Если переменная не найдена, подставляется дефолтное значение (например, "postgres" или хост "booking_db").
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_HOST = os.getenv("DB_HOST", "booking_db")  # Имя сервиса базы данных из docker-compose.yml
DB_PORT = os.getenv("DB_PORT", "5432")

ASYNC_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Передаем собранный URL в конфигурацию Alembic напрямую в память (без записи на диск)
config.set_main_option("sqlalchemy.url", ASYNC_DATABASE_URL)

# Настройка логирования на основе файла конфигурации alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Передаем метадату моделей, чтобы работали автоматические миграции
target_metadata = Base.metadata


def do_run_migrations(connection):
    """Выполнение миграций в контексте синхронного соединения."""
    context.configure(
        connection=connection, 
        target_metadata=target_metadata
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Запуск миграций в асинхронном режиме (Online-режим)."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        # Поскольку Alembic работает синхронно, запускаем функцию через враппер run_sync
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


# Запускаем асинхронный цикл для выполнения миграций
asyncio.run(run_migrations_online())
