import pytest
from app import app, todos


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    todos.clear()
    todos.append({"id": 1, "task": "Test task", "completed": False})
    with app.test_client() as test_client:
        yield test_client


def test_home_returns_success(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Todo API is running"


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_get_todos_returns_list(client):
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_post_todo_creates_task(client):
    response = client.post("/todos", json={"task": "Learn Docker"})
    assert response.status_code == 201
    assert response.get_json()["task"] == "Learn Docker"


def test_post_todo_rejects_empty_task(client):
    response = client.post("/todos", json={"task": " "})
    assert response.status_code == 400
