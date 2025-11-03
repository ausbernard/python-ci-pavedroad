from fastapi.testclient import TestClient

from python_ci_pavedroad_template_app.app import app

client = TestClient(app)


def test_list_users():
    """
    RED phase: This test will fail because /users endpoint doesn't exist yet
    """
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == {"users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}


def test_get_user():
    """
    RED phase: This test will fail because /users/{id} endpoint doesn't exist yet
    """
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Alice"}


def test_user_not_found():
    """
    RED phase: This test will fail, but it's important to test error cases too
    """
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
