# test_coffee_api.py
import pytest
import requests
 
@pytest.mark.smoke
@pytest.mark.parametrize("size, expected_status, expected_price", [
    pytest.param("small", 200, 2.5, id="small_ok"),
    pytest.param("medium", 200, 3.5, id="medium_ok"),
    pytest.param("extra_large", 400, None, id="extra_large_bad"),
])
def test_get_coffee(size, expected_status, expected_price, base_url):
    response = requests.get(f"{base_url}/coffee/{size}")
    assert response.status_code == expected_status
    if expected_status == 200:
        assert response.json()["price"] == expected_price
    else:
        assert "error" in response.json() 
