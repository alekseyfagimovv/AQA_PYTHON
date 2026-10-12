# # conftest

# from src.tests.other.shopping import ShoppingCart

# import pytest
# import tempfile
# import os


# @pytest.fixture(scope="function")
# def cart():
#     cart = ShoppingCart()
#     yield cart
#     cart.items().clear()
#     print("cart cleaned")

# @pytest.fixture(scope="function")
# def temp_file():
#     fp = tempfile.NamedTemporaryFile(mode='w+t',
#                                    delete=False)
#     path = fp.name
#     yield fp
#     fp.close()
#     os.remove(path)
#     print('file delete')

# @pytest.fixture(scope='function')
# def base_url():
#     return "http://localhost:8000"


import pytest

@pytest.fixture
def valid_password():
    return "gfdgs1235F"

@pytest.fixture
def invalid_passwords():
    return [
        ("gfdF", "too short"),
        ("gfdd12345", "no uppercase"),
        ("fdfbFdsdsu", "no digit"),
        ("", "too short"),
    ]


@pytest.fixture(scope="module")
def module_marker():
    print("\n[SETUP] module_marker создан")
    yield "marker"
    print("\n[TEARDOWN] module_marker уничтожен")

# ********************************
from routers.cinema import TaskRepo


@pytest.fixture(scope="function")
def test_repo():
    repo = TaskRepo()
    yield repo
    repo._store.clear()