# test_shopping

def test_cart_empty_initially(cart):
    assert cart.items() == []

def test_cart_add_item(cart):
    item = "apple"
    cart.add(item)
    assert cart.items() == ["apple"]

def test_cart_remove_item(cart):
    item = "apple"
    cart.add(item)
    cart.remove(item)
    assert cart.items() == []

def test_cart_isolation(cart):
    item = "apple"
    cart.add(item) 
    assert cart.items() == ["apple"]

def test_cart_temp_file_written(temp_file):
    temp_file.write("hello")
    temp_file.seek(0)
    assert temp_file.read() == "hello"
