import pytest
import request

def test_create_room_valid(base_url):
    
    # Делает POST на /rooms/ с именем комнаты "QA Room".
    # Проверяет: статус-код 201 и что в ответе (response.json()) есть ключ id.

def test_get_bookings_by_room(base_url):
#   Делает GET на /bookings/room/1 (или любой другой ID).
#   Проверяет: статус-код 200 и что ответ является списком (isinstance(response.json(), list)).

@pytest.mark.xfail
def test_create_booking_in_past(base_url):
    # Делает POST на /bookings/ с датой из прошлого (например, 2020-01-01T10:00:00Z).
    # Проверяет: статус-код 400 или 422 (потому что в прошлом бронировать нельзя).
    # Внимание: Этот тест должен упасть. Так ты докажешь, что баг, который мы нашли руками, воспроизводится в автоматике.
