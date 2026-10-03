# import pytest


# def make_counter(start=0):
#     count = start
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter

# @pytest.mark.parametrize("start", [0, 1])
# def test_make_counter(start):
#     counter = make_counter(start)
#     assert counter() == start + 1
#     assert counter() == start + 2

# def make_adder(n):
#     def adder(x):
#         return n + x
#     return adder


# @pytest.mark.parametrize("n, x, expected", [
#     (1, 2, 3),
#     (0, 5, 5),
#     (-1, 10, 9),
# ])
# def test_make_adder(n, x, expected):
#     adder = make_adder(n)
#     assert adder(x) == expected




# # ***********************************************
# import smtplib
# from unittest.mock import MagicMock

# from coffee_shop.notifier import send_order_confirmation


# def test_send_confirmation_success(mocker):
#     mock_smtp = mocker.patch("coffee_shop.notifier.smtplib.SMTP")
#     result = send_order_confirmation("user@test.com", 42)
#     assert result is True
#     mock_smtp.assert_called_once()

# def test_send_confirmation_smtp_error(mocker):
#     mock_smtp = mocker.patch("coffee_shop.notifier.smtplib.SMTP")
#     mock_smtp.side_effect = smtplib.SMTPException("connection refused")
#     result = send_order_confirmation("user@test.com", 42)
#     assert result is False

# def test_send_confirmation_uses_correct_recipient(mocker):
#     mock_smtp_class = mocker.patch("coffee_shop.notifier.smtplib.SMTP")
#     smtp_instance = mock_smtp_class.return_value.__enter__.return_value
#     send_order_confirmation("user@test.com", 42)
#     smtp_instance.sendmail.assert_called_once_with("robot@coffee.shop", "user@test.com", "Your order #42 is confirmed")

# # ***************************************************************

 

# from src.routers.fetch_user import fetch_user


# def test_fetch_user(mocker):
#     mock_get = mocker.patch(
#         "src.routers.fetch_user.requests.get",
#         return_value=mocker.Mock(json=lambda: {"id": 1, "name": "Alice"})
#     )
#     result = fetch_user(1)
#     assert result == {"id": 1, "name": "Alice"}
#     mock_get.assert_called_once_with("https://api.example.com/users/1")

# import pytest
# import requests

# def test_fetch_user_connection_error(mocker):
#     mocker.patch(
#         "src.routers.fetch_user.requests.get",
#         side_effect=requests.exceptions.ConnectionError
#     )
    
#     with pytest.raises(requests.exceptions.ConnectionError):
#         fetch_user(1)

# # *****************
 

# from src.routers.fetch_user import get_user_name


# def test_get_user_name(mocker):
#     fake_resp = mocker.MagicMock()
#     fake_resp.json.return_value = {"name": "Alice"}

#     mock_get = mocker.patch(
#         "src.routers.fetch_user.requests.get",  # Нужно импортировать от места фактического использования функции
#         return_value=fake_resp
#     )
#     result = get_user_name(42) 
#     assert result == "Alice"
#     mock_get.assert_called_once_with("https://api.example.com/users/42")


from unittest.mock import MagicMock


fake_resp = MagicMock() 
fake_resp.json.return_value = {"name": "Alice"}

fake_requests_get = MagicMock(return_value=fake_resp)

resp = fake_requests_get("http://x/1")
print(resp)
print(resp.json())
print(fake_requests_get.call_args)