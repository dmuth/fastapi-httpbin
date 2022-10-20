
import json

from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)


def test_anything_get():

    response = client.get("/anything")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["verb"] == "GET"

    response = client.get("/anything?test=test2")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["args"]["test"] == "test2"
    assert response.json()["verb"] == "GET"


def test_anything_post():

    data = { "cheetah": "chirp", "goat": "bleat" }

    response = client.post("/anything", json = json.dumps(data))
    assert response.status_code == 200
    data = json.loads(response.json()["data"])
    assert data["cheetah"] == "chirp"
    assert response.json()["verb"] == "POST"

    data = [ data ]

    response = client.post("/anything", json = json.dumps(data))
    assert response.status_code == 200
    data = json.loads(response.json()["data"])
    assert data[0]["cheetah"] == "chirp"
    assert response.json()["verb"] == "POST"


def test_anything_put():
    data = { "cheetah": "chirp", "goat": "bleat" }

    response = client.put("/anything", json = json.dumps(data))
    assert response.status_code == 200
    data = json.loads(response.json()["data"])
    assert data["cheetah"] == "chirp"
    assert response.json()["verb"] == "PUT"

    data = [ data ]

    response = client.put("/anything", json = json.dumps(data))
    assert response.status_code == 200
    data = json.loads(response.json()["data"])
    assert data[0]["cheetah"] == "chirp"
    assert response.json()["verb"] == "PUT"


def test_anything_patch():
    data = { "cheetah": "chirp", "goat": "bleat" }

    response = client.patch("/anything", json = json.dumps(data))
    assert response.status_code == 200
    data = json.loads(response.json()["data"])
    assert data["cheetah"] == "chirp"
    assert response.json()["verb"] == "PATCH"

    data = [ data ]

    response = client.patch("/anything", json = json.dumps(data))
    assert response.status_code == 200
    data = json.loads(response.json()["data"])
    assert data[0]["cheetah"] == "chirp"
    assert response.json()["verb"] == "PATCH"


def test_anything_delete():

    response = client.delete("/anything")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["verb"] == "DELETE"



