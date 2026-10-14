# import pytest
# from fastapi.testclient import TestClient
# from routers.cinema import app


# @pytest.fixture(scope="function")
# def client():
#     return TestClient(app)

# # get_bug, transition_bug, create_bug, delete_bug

# def test_direct_traffic_ban(client):
#     response = client.post("/bugs", json={
#     "title": "Баг прямой трафик бан",
#     "severity": "Critical",
#     "priority": "Medium"
# }) 
#     assert response.status_code == 201
#     bug_id = response.json()["id"]
#     response = client.post(f"/bugs/{bug_id}/transition", json={"to_status": "Closed"})
#     assert response.status_code == 409
#     response = client.get(f"/bugs/{bug_id}")
#     assert response.json()["status"] == "New"
#     response = client.delete(f"/bugs/{bug_id}")
#     assert response.status_code == 204


# def test_automatic_priority_increase_when_reopened(client):
#     responce = client.post("/bugs", json={
#     "title": "Баг приоритет переоткрытия",
#     "severity": "Critical",
#     "priority": "Low"
#     })
#     bug_id = responce.json()["id"]

#     chain = ["Assigned", "In Progress", "Fixed", "Ready for QA", "Verified", "Closed", "Reopened"]
#     for status in chain:
#         response = client.post(f"/bugs/{bug_id}/transition", json={"to_status": status})
#         assert response.status_code == 200  
#         assert response.json()["status"] == status  
#     responce = client.get(f"/bugs/{bug_id}")

#     assert  responce.json()["status"] == "Reopened"
#     assert  responce.json()["priority"] == "High"

#     response = client.delete(f"/bugs/{bug_id}")
#     assert response.status_code == 204 

# def test_get_nonexistent_bug_returns_404(client):
#     responce = client.get("/bugs/99999")
#     assert responce.status_code == 404
#     assert responce.json()["detail"] == "Bug not found"

 
# import pytest

# @pytest.mark.parametrize("name", [
#     pytest.param("Задача", id='task'),
#     pytest.param("", id='Пустота'),
#     pytest.param(" пробелы ", id=' пробелы '),
# ])
# def test_add_and_get(test_repo, name):
#     test_repo.add(name)
#     assert name == test_repo.get(1)["title"]

# @pytest.mark.sleep
# def test_true(test_repo):
#     test_repo.add("Задача")
#     assert test_repo.mark_done(1) is True
#     assert test_repo.get(1)["done"] is True

# test_cinema.py

import pytest

@pytest.mark.parametrize("meaning, result, code", [
    pytest.param(-1, -1, 400, id="-1, -1"),
    pytest.param(0, 0, 400, id="0, 0"),
    pytest.param(1, 1, 201, id="1, 1"),
    pytest.param(9, 9, 201, id="9, 9"),
    pytest.param(10, 10, 201, id="10, 10"),
    pytest.param(11, 11, 400, id="11, 11"),
])
def test_create_order_valid_and_no_valid(create_order, meaning, result, code):
    response = create_order(meaning)
    assert response.status_code == code
    if code == 201:
        assert response.json()["quantity"] == result
    if code == 400:
        assert response.json()["detail"] == "quantity must be between 1 and 10"


def test_get_order_success_and_no_success(create_order, get_data):
    response_post = create_order(1)
    assert response_post.status_code == 201
    response_get = get_data(response_post.json()["id"])
    assert response_get.status_code == 200
    assert response_get.json() == {"id": response_post.json()["id"],
        "status": "created",
        "quantity": 1,
        "message": "Принято 1 чашек кофе"}
    response_get = get_data(999999)
    assert response_get.status_code == 404
    assert response_get.json()["detail"] == "order not found"
    
def test_delete_order_success_and_no_success(create_order, delete_data):
    response_post = create_order(1)
    assert response_post.status_code == 201
    response_delete = delete_data(response_post.json()["id"])
    assert response_delete.status_code == 204
    response_delete = delete_data(999999)
    assert response_delete.status_code == 404
    assert response_delete.json()["detail"] == "order not found"








