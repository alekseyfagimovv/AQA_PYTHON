# conftest

from tests.shopping import ShoppingCart

import pytest
import tempfile
import os


@pytest.fixture(scope="function")
def cart():
    cart = ShoppingCart()
    yield cart
    cart.items().clear()
    print("cart cleaned")

@pytest.fixture(scope="function")
def temp_file():
    fp = tempfile.NamedTemporaryFile(mode='w+t',
                                   delete=False)
    path = fp.name
    yield fp
    fp.close()
    os.remove(path)
    print('file delete')

