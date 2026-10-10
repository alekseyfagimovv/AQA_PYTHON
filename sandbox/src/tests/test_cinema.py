import pytest
from fastapi.testclient import TestClient
from routers.cinema import app


@pytest.fixture(scope="function")
def client():
    return TestClient(app)

# get_bug, transition_bug, create_bug, delete_bug

def test_direct_traffic_ban(client):
    response = client.post("/bugs", json={
    "title": "Баг прямой трафик бан",
    "severity": "Critical",
    "priority": "Medium"
}) 
    assert response.status_code == 201
    bug_id = response.json()["id"]
    response = client.post(f"/bugs/{bug_id}/transition", json={"to_status": "Closed"})
    assert response.status_code == 409
    response = client.get(f"/bugs/{bug_id}")
    assert response.json()["status"] == "New"
    response = client.delete(f"/bugs/{bug_id}")
    assert response.status_code == 204


def test_automatic_priority_increase_when_reopened(client):
    responce = client.post("/bugs", json={
    "title": "Баг приоритет переоткрытия",
    "severity": "Critical",
    "priority": "Low"
    })
    bug_id = responce.json()["id"]

    chain = ["Assigned", "In Progress", "Fixed", "Ready for QA", "Verified", "Closed", "Reopened"]
    for status in chain:
        response = client.post(f"/bugs/{bug_id}/transition", json={"to_status": status})
        assert response.status_code == 200  
        assert response.json()["status"] == status  
    responce = client.get(f"/bugs/{bug_id}")

    assert  responce.json()["status"] == "Reopened"
    assert  responce.json()["priority"] == "High"

    response = client.delete(f"/bugs/{bug_id}")
    assert response.status_code == 204 

def test_get_nonexistent_bug_returns_404(client):
    responce = client.get("/bugs/99999")
    assert responce.status_code == 404
    assert responce.json()["detail"] == "Bug not found"

 










