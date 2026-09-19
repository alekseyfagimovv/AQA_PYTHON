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
