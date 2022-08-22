
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)

#
# This is our main function which performs all of the tests.
#
# cb - The callback to the request method.
#
def core(cb):

    response = client.get("/redirect/1", allow_redirects = False)
    assert response.status_code == 200
    assert response.json()["message"] == "Reached the end of our redirects!"

    response = client.get("/redirect/2", allow_redirects = False)
    assert response.status_code == 302
    assert response.headers["location"] == "/redirect/1"

    response = client.get("/redirect/5", allow_redirects = False)
    assert response.status_code == 302
    assert response.headers["location"] == "/redirect/4"

    response = client.get("/redirect", allow_redirects = False)
    assert response.status_code == 404

    response = client.get("/redirect/", allow_redirects = False)
    assert response.status_code == 404

    response = client.get("/redirect/cheetah", allow_redirects = False)
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "type_error.integer"

    response = client.get("/redirect/21", allow_redirects = False)
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "value_error.int.max_size"


def test_get():
    core(client.get)

def test_post():
    core(client.post)

def test_put():
    core(client.put)

def test_patch():
    core(client.patch)

def test_delete():
    core(client.delete)


