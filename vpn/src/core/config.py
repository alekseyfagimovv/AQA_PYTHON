# core/config.py
    # Сюда прилетают параметры из .env
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_login: str
    db_password: str
    debug: bool = False  # значение по умолчанию, если не найдётся

    # Говорим, что читать из файла .env
    model_config = SettingsConfigDict(env_file=".env")

# Создаём один объект настроек на весь проект
settings = Settings()