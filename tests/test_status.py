
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)

def test_get():

    response = client.get("/status/200")
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

    response = client.get("/status/201,202,203,401,404")
    assert response.status_code in [201, 202, 203, 401, 404]

    response = client.get("/status/1")
    assert response.json()["detail"][0]["type"] == "value_error.any_str.min_length"

    response = client.get("/status/cheetah,goat")
    assert response.json()["detail"][0]["type"] == "value_error.str.regex"

    response = client.get("/status/200,2001,300")
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "code_length"

    response = client.get("/status/200,1,300")
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "code_length"

    response = client.get("/status")
    assert response.status_code == 404

# X how to set redirect header?
# X how to test for redirect header?
# X write GET endpoint
# X do multiple statuses with random pick
# X throw invalid data and test with a regex validator
# X test min_length
# X what happens with a code > 3 digits, do I have to check for it?
# X Catch not having any parameter supplied
# put tests into function
# write additional tests


