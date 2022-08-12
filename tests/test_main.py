
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == { "Hello": "World"}

def test_get_get():
    response = client.get("/get")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"

def test_get_delete():
    response = client.delete("/delete")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"

def test_get_patch():
    response = client.patch("/patch")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"

def test_get_post():
    response = client.post("/post")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"

def test_get_put():
    response = client.put("/put")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"


