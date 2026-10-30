# # test_coffee_api.py
# import pytest
# import requests
 
# @pytest.mark.smoke
# @pytest.mark.parametrize("size, expected_status, expected_price", [
#     pytest.param("small", 200, 2.5, id="small_ok"),
#     pytest.param("medium", 200, 3.5, id="medium_ok"),
#     pytest.param("extra_large", 400, None, id="extra_large_bad"),
# ])
# def test_get_coffee(size, expected_status, expected_price, base_url):
#     response = requests.get(f"{base_url}/coffee/{size}")
#     assert response.status_code == expected_status
#     if expected_status == 200:
#         assert response.json()["price"] == expected_price
#     else:
#         assert "error" in response.json() 


# from src.routers.fetch_user import validate_password
# import pytest


# @pytest.mark.parametrize("password, expected_valid, expected_result", [
#     pytest.param("gfdgs1235F", True, "ok", id="validate"),
#     pytest.param("gfdF", False, "too short", id="too short"),
#     pytest.param("gfdd12345", False, "no uppercase", id="no uppercase"),
#     pytest.param("fdfbFdsdsu", False, "no digit", id="no digit"),
#     pytest.param("Abcdefg1", True, "ok", id="exactly 8 chars"),
#     pytest.param("", False, "too short", id="too short ''"),
# ])
# def test_validate_password(password, expected_valid, expected_result):
#     assert validate_password(password) == (expected_valid, expected_result)
    
# def test_none_password():
#     with pytest.raises(TypeError):
#         validate_password(None)


# def test_valid_password_via_fixture(valid_password):
#     assert validate_password(valid_password) == (True, "ok")

# def test_invalid_passwords_via_fixture(invalid_passwords):
#     for pwd, expected_msg in invalid_passwords:
#         assert validate_password(pwd) == (False, expected_msg)


# def test_a(module_marker):
#     assert module_marker == "marker"

# def test_b(module_marker):
#     assert module_marker == "marker"