import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_predict_endpoint_valid():
    response = client.post("/predict", json={"feature1": 1.0})
    assert response.status_code == 200
    json_resp = response.json()
    assert "prediction" in json_resp
    assert isinstance(json_resp["prediction"], float)

def test_predict_endpoint_invalid_type():
    # feature1 должен быть float, передаём строку — ожидаем 422
    response = client.post("/predict", json={"feature1": "invalid"})
    assert response.status_code == 422

def test_predict_endpoint_missing_feature():
    # Пропускаем feature1 — тоже 422
    response = client.post("/predict", json={})
    assert response.status_code == 422

def test_predict_endpoint_negative_feature():
    # feature1 < 0 — из-за ge=0.0 в модели Pydantic должно вернуть 422
    response = client.post("/predict", json={"feature1": -1.0})
    assert response.status_code == 422
