
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

    headers_json = {"Content-Type": "application/json"}
    headers_form = {"Content-Type": "application/x-www-form-urlencoded"}

    data = {}
    response = client.post("/post", json = json.dumps(data), headers = headers_json)
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data == {}

    data = "broken json"
    response = client.post("/post", json = json.dumps(data), headers = headers_json)
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data == "broken json"

    data = { "cheetah": "chirp", "goat": "bleat" }
    response = client.post("/post", json = json.dumps(data), headers = headers_json)
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = json.loads(response.json()["data"])
    assert data["cheetah"] == "chirp"

    data = [ data ]
    response = client.post("/post", json = json.dumps(data), headers = headers_json)
    assert response.status_code == 200
    data = json.loads(response.json()["data"])
    assert data[0]["cheetah"] == "chirp"

    #
    # Test regular form data
    #
    form_data = "birthyear=1905&press=%20OK%20"
    response = client.post("/post", data = form_data, headers = headers_form)
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    data = response.json()["data"]
    assert data["birthyear"][0] == "1905"
    assert data["press"][0] == " OK "


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


