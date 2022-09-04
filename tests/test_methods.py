
import json

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

    data = {}
    response = client.post("/post", json = json.dumps(data))
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data == {}

    data = "broken json"
    response = client.post("/post", json = json.dumps(data))
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data == "broken json"

    data = { "cheetah": "chirp", "goat": "bleat" }

    response = client.post("/post", json = json.dumps(data))
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data["cheetah"] == "chirp"

    data = [ data ]

    response = client.post("/post", json = json.dumps(data))
    assert response.status_code == 200
    data = json.loads(response.json()["data"])
    assert data[0]["cheetah"] == "chirp"


def test_put():

    data = {}
    response = client.put("/put", json = json.dumps(data))
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data == {}

    data = "broken json"
    response = client.put("/put", json = json.dumps(data))
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data == "broken json"

    data = { "cheetah": "chirp", "goat": "bleat" }

    response = client.put("/put", json = json.dumps(data))
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data["cheetah"] == "chirp"

    data = [ data ]

    response = client.put("/put", json = json.dumps(data))
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data[0]["cheetah"] == "chirp"


def test_patch():

    data = {}
    response = client.patch("/patch", json = json.dumps(data))
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data == {}

    data = "broken json"
    response = client.patch("/patch", json = json.dumps(data))
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data == "broken json"

    data = { "cheetah": "chirp", "goat": "bleat" }

    response = client.patch("/patch", json = json.dumps(data))
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data["cheetah"] == "chirp"

    data = [ data ]

    response = client.patch("/patch", json = json.dumps(data))
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data[0]["cheetah"] == "chirp"


def test_delete():
    response = client.delete("/delete")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"


