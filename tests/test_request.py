
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)

def test_headers():
    response = client.get("/headers")
    assert response.status_code == 200
    assert response.json()["host"] == "testserver"

def test_ip():
    response = client.get("/ip")
    assert response.status_code == 200
    assert response.json()["ip"] == "testclient"

    response = client.get("/ip", headers = {"x-forwarded-for": "1.2.3.4"})
    assert response.status_code == 200
    assert response.json()["ip"] == "1.2.3.4"

def test_user_agent():
    response = client.get("/user-agent")
    assert response.status_code == 200
    assert response.json()["user-agent"] == "testclient"


