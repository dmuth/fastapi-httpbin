
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


def test_get(mocker):

    setup_test_client(mocker)

    response = client.get("/get")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"
    assert len(response.json()["args"]) == 0
    assert "_comment" in response.json()

    response = client.get("/get?test1=test2&test3=test4")
    assert response.status_code == 200
    assert response.json()["args"]["test1"] == "test2"
    assert len(response.json()["args"]) == 2


def test_get_args(mocker):

    setup_test_client(mocker)

    response = client.get("/get/args")
    assert response.status_code == 200
    assert "headers" not in response.json()
    assert "source" not in response.json()
    assert "url" not in response.json()
    assert len(response.json()) == 0

    response = client.get("/get/args?test1=test2&test3=test4")
    assert response.status_code == 200
    assert response.json()["test1"] == "test2"
    assert len(response.json()) == 2


def test_post(mocker):

    setup_test_client(mocker)

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


def test_put(mocker):

    setup_test_client(mocker)

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


def test_patch(mocker):

    setup_test_client(mocker)

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


def test_delete(mocker):

    setup_test_client(mocker)

    response = client.delete("/delete")
    assert response.status_code == 200
    assert response.json()["source"]["ip"] == "testclient"
    assert response.json()["headers"]["host"] == "testserver"


