
import hashlib
import json

from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)


def test_form_post():

    data = {}
    response = client.post("/form/post", data = data)
    assert response.status_code == 422
   
    data = {"username": "dmuth1", "password": "password1"}
    response = client.post("/form/post", data = data)
    assert response.status_code == 401
   
    data = {"username": "dmuth", "password": "password"}
    response = client.post("/form/post", data = data)
    assert response.status_code == 200


