# 1. Сначала импортируем Base
from src.models.base import Base

# 2. Затем импортируем модели. Теперь они линейно унаследуются от уже созданного Base!
from src.models.booking import RoomModel, BookingModel

# 3. Явно перечисляем их для внешних модулей
__all__ = ["Base", "RoomModel", "BookingModel"]