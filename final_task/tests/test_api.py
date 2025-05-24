import pytest
from fastapi.testclient import TestClient
from final_task.api import app

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/predict", json={"feature1": 1.0})
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert isinstance(response.json()["prediction"], float)

def test_invalid_input():
    response = client.post("/predict", json={"feature1": "invalid"})
    assert response.status_code == 422