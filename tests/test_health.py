from fastapi.testclient import TestClient

from python_ci_pavedroad_template_app.app import app

client = TestClient(app)


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}
