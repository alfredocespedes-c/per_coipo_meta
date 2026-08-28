from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["ok"] is True
    assert "facebook" in body["channels"]


def test_protected_without_api_key() -> None:
    response = client.post(
        "/facebook/posts",
        json={"app_name": "forestin_informa", "message": "Prueba"},
    )
    assert response.status_code == 401


def test_mock_facebook_publish() -> None:
    response = client.post(
        "/facebook/posts",
        headers={"X-API-Key": "forestin-meta-poc"},
        json={
            "app_name": "forestin_informa",
            "campaign_id": "INC-2026-001",
            "message": "CONAF informa actualización de incendio forestal.",
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["ok"] is True
    assert body["channel"] == "facebook"
    assert body["status"] == "mocked"
