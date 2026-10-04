import requests

def fetch_user(user_id: int) -> dict:
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

# *******************

import requests

def get_user_name(user_id: int) -> str:
    resp = requests.get(f"https://api.example.com/users/{user_id}")
    data = resp.json()
    return data["name"]

# *******************************

import httpx

def get_user_city(user_id: int) -> str:
    """Возвращает название города пользователя из внешнего API."""
    resp = httpx.get(f"https://api.example.com/users/{user_id}")
    resp.raise_for_status()
    data = resp.json()
    return data["address"]["city"]