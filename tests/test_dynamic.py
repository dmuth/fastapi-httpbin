
import json
from unittest.mock import AsyncMock

from fastapi.testclient import TestClient


from main import app

client = TestClient(app)


def test_uuid():
    response = client.get("/uuid")
    assert response.status_code == 200
    assert "uuid" in response.json()
    assert "-4" in response.json()["uuid"]
    assert "random.org" in response.json()["message"]


def test_delay():
    response = client.get("/delay/2?debug=1")
    assert response.status_code == 200
    assert "2 seconds" in response.json()["message"]

    response = client.get("/delay/10?debug=1")
    assert response.status_code == 200
    assert "10 seconds" in response.json()["message"]

    response = client.get("/delay/0?debug=1")
    assert response.status_code == 200
    assert "0 seconds" in response.json()["message"]

    response = client.get("/delay/11?debug=1")
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "value_error.int.max_size"

    response = client.get("/delay/-1?debug=1")
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "value_error.int.min_size"


def test_stream():

    response = client.get("/stream/5")
    assert response.status_code == 200
    lines = response.text.split("\n")
    assert len(lines) == 6
    line = lines[1]    
    row = json.loads(line)
    assert row["response_number"] == 2
    assert "-4" in row["uuid"]

    response = client.get("/stream/-1")
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "value_error.int.min_size"
    
    response = client.get("/stream/0")
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "value_error.int.min_size"
    
    response = client.get("/stream/101")
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "value_error.int.max_size"
    


