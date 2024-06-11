
import json

from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)


#
# Set up a fake request client
#
def setup_test_client(mocker):
    mock_client = mocker.patch("fastapi.Request.client")
    mock_client.host = "testclient"
    mock_client.port = "12345"



def test_anything_get(mocker):

    setup_test_client(mocker)

    response = client.get("/anything")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["verb"] == "GET"

    response = client.get("/any")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["verb"] == "GET"

    assert response.headers["x-fastapi-httpbin-version"] != None
    assert response.headers["x-website"] == "https://httpbin.dmuth.org/"
    #
    # An empty string is returned by the underlying platform.node() call if
    # a hostname cannot be determined, but I don't ever expect that to be 
    # an issue in Docker/testing.
    #
    assert response.headers["x-app-hostname"] != None
    assert response.headers["x-app-hostname"] != ""

    response = client.get("/anything?test=test2")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["args"]["test"] == "test2"
    assert response.json()["verb"] == "GET"


def test_anything_head(mocker):

    setup_test_client(mocker)

    response = client.head("/anything")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.text == ""

    response = client.head("/any")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.text == ""


def test_anything_post(mocker):

    setup_test_client(mocker)

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


def test_anything_put(mocker):

    setup_test_client(mocker)

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


def test_anything_patch(mocker):

    setup_test_client(mocker)

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


def test_anything_delete(mocker):

    setup_test_client(mocker)

    response = client.delete("/anything")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["verb"] == "DELETE"



