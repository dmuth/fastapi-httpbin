
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

    response = cb("/status/200")
    assert response.status_code == 200

    response = client.get("/status/204")
    assert response.status_code == 204

    response = client.get("/status/301", allow_redirects = False)
    assert response.status_code == 301
    assert response.headers["location"] == "/redirect/1"

    response = client.get("/status/404")
    assert response.status_code == 404

    response = client.get("/status/510")
    assert response.status_code == 510

    response = client.get("/status/201,202")
    assert response.status_code in [201, 202]

    response = client.get("/status/201,202,203,401,404")
    assert response.status_code in [201, 202, 203, 401, 404]

    response = client.get("/status/211_212")
    assert response.status_code in [211, 212]

    response = client.get("/status/211_212_213_411_414")
    assert response.status_code in [211, 212, 213, 411, 414]

    response = client.get("/status/1")
    assert response.json()["detail"][0]["type"] == "string_too_short"

    response = client.get("/status/cheetah,goat")
    assert response.json()["detail"][0]["type"] == "string_pattern_mismatch"

    response = client.get("/status/200,2001,300")
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "code_length"

    response = client.get("/status/200,1,300")
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "code_length"

    response = client.get("/status")
    assert response.status_code == 404


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


