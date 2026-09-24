# Есть модуль library.py с функцией:

def borrow_book(book_id: int, user_id: int) -> dict:
    # """Выдаёт книгу пользователю.
    # Возвращает {'book_id': book_id, 'user_id': user_id, 'status': 'borrowed'}.
    # Если book_id <= 0 — ValueError с текстом 'book_id must be positive'.
    # Если user_id <= 0 — ValueError с текстом 'user_id must be positive'.
    # """
    if book_id <= 0:
        raise(ValueError("book_id must be positive"))
    elif user_id <= 0:
        raise(ValueError("user_id must be positive"))
    else:
        return {'book_id': book_id, 'user_id': user_id, 'status': 'borrowed'}
# Файл test_library.py с тестами
#  Успешная выдача книги — проверь все три поля результата.
# book_id = 0 бросает ValueError с правильным сообщением.
# user_id = -5 бросает ValueError с правильным сообщением.
# Ограничения: каждый тест — отдельная функция. Без параметризации. 
# Используй pytest.raises с match там, где нужно. Имена файла и функций — по правилам pytest.

 
def test_borrow_book_success():
    result = borrow_book(200, 1)
    assert result["book_id"] == 200
    assert result["user_id"] == 1
    assert result["status"] == "borrowed"

def test_borrow_book_invalid_book_id():
    with pytest.raises(ValueError, match="book_id must be positive"):
        assert borrow_book(0, 5)

def test_borrow_invalid_user_id():
    with pytest.raises(ValueError, match="user_id must be positive"):
        borrow_book(5, -5)

#  Напиши фикстуру book_factory для библиотеки.

import pytest

@pytest.fixture(scope="function")
def book_factory():
    counter = 0
    created = []   

    def create(title):
        nonlocal counter
        counter += 1
        book = {"id": counter, "title": title}
        created.append(book) 
        print(f"Создана книга: {book}")
        return book

    yield create
    for book in created:
        print(f"Удалена книга: {book['id']}")
    print("Teardown: все книги удалены")


def test_two_books_different_id(book_factory):
    one_book = book_factory("First")
    second_book = book_factory("Two")
    assert second_book['id'] != one_book['id']

def test_book_factory_check_title(book_factory):
    result = book_factory("First")
    assert result['title'] == "First"

# Проверка работы ручек эдпоинта с параметризацией 
from fastapi import FastAPI, HTTPException
import pytest
from fastapi.testclient import TestClient

app = FastAPI()

ROOMS = {1: {"id": 1, "name": "A"}, 2: {"id": 2, "name": "B"}}

@app.get("/rooms/{room_id}")
async def get_rooms(room_id: int):
    if room_id in ROOMS:
        return ROOMS[room_id]
    raise HTTPException(status_code=404)

@pytest.fixture(scope="module")
def rooms_data():
    return ROOMS

@pytest.fixture(scope="module")
def client():
    return TestClient(app)

@pytest.fixture(scope="function")
def first_room():
    return ROOMS[1]["id"]

def test_get_existing_room(client, first_room: int, rooms_data: dict[int, dict]):
    response = client.get(f"/rooms/{first_room}")
    assert response.status_code == 200  
    assert response.json()["name"] == rooms_data[first_room]["name"]   


@pytest.mark.parametrize("unknown_id, expected", [(-1, 404), (0, 404), (999, 404)])
def test_get_unknown_room(client, unknown_id, expected):
    response = client.get(f"/rooms/{unknown_id}")
    assert response.status_code == expected

# defaul assert + raise tests
import pytest


def add(a, b):
    return a + b 

def test_add_two_positive():
    assert add(2, 3) == 5

def test_add_with_zero():
    assert add(0, 7) == 7

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_raises_on_string():
    with pytest.raises(TypeError):
        add("2", 3)

# test marks n' ini file 'n raise + assert
import pytest

def multiply(a, b):
    return a * b    

def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

@pytest.mark.smoke
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(0, 0) == 0

@pytest.mark.smoke
def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(-10, 2) == -5.0
    assert divide(0, 5) == 0.0
    assert divide(7, 2) == 3.5

@pytest.mark.smoke
def test_divide_by_zero():
    with pytest.raises(ValueError, match="division by zero"):
        divide(5, 0)
