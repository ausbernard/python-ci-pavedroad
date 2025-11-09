from fastapi.testclient import TestClient

from python_ci_pavedroad_template_app.app import app

client = TestClient(app)


def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "Welcome to the home screen!", "health_url": "/health"}
