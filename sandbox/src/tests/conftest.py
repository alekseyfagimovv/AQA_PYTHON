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


# import pytest

# @pytest.fixture
# def valid_password():
#     return "gfdgs1235F"

# @pytest.fixture
# def invalid_passwords():
#     return [
#         ("gfdF", "too short"),
#         ("gfdd12345", "no uppercase"),
#         ("fdfbFdsdsu", "no digit"),
#         ("", "too short"),
#     ]


# @pytest.fixture(scope="module")
# def module_marker():
#     print("\n[SETUP] module_marker создан")
#     yield "marker"
#     print("\n[TEARDOWN] module_marker уничтожен")

# # ********************************
# from routers.cinema import TaskRepo


# @pytest.fixture(scope="function")
# def test_repo():
#     repo = TaskRepo()
#     yield repo
#     repo._store.clear()

# # confest.py

# import pytest
# from fastapi.testclient import TestClient

# from routers.coffee_api import app
# from routers.coffee_api import _orders

# @pytest.fixture(scope="function")
# def client():
#     return TestClient(app)

# @pytest.fixture(scope="function")
# def create_order(client):
#     order_data = None
#     def make_post(quantity):
#         response = client.post("/coffee/order", json={"quantity": quantity}) 
#         nonlocal order_data
#         order_data = response
#         return response
#     yield make_post
#     if order_data is not None and order_data.status_code == 201:
#         _orders.pop(order_data.json()["id"], None)


# @pytest.fixture(scope="function")
# def get_data(client):
#     def make_get(order_id):
#         response = client.get(f"/coffee/order/{order_id}") 
#         return response
#     yield make_get

# @pytest.fixture(scope="function")
# def delete_data(client):
#     def make_delete(order_id):
#         response = client.delete(f"/coffee/order/{order_id}") 
#         return response
#     yield make_delete




