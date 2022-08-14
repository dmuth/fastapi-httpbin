
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)

def test_get():
    response = client.get("/get")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"

def test_post():
    response = client.post("/post")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"

def test_put():
    response = client.put("/put")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"

def test_patch():
    response = client.patch("/patch")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"

def test_delete():
    response = client.delete("/delete")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"


