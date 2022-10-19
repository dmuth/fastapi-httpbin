
import hashlib
import json

from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)


def test_qrcode_post():

    response = client.post("/qrcode/json")
    assert response.status_code == 422

    data = {"url": "https://www.youtube.com/watch?v=nCEemcXzERk", "box_size": 10, "border": 2}
    response = client.post("/qrcode/json", json = data)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    response_body = b""
    for chunk in response.iter_content():
        response_body += chunk
    hash = hashlib.sha1(response_body).hexdigest()
    assert hash == "b7f494872858b727905fadc1137a8b3dea596ad9"


def test_qrcode_get():
    response = client.get("/qrcode", allow_redirects = False)
    assert response.status_code == 302
    assert response.headers["location"] == "/qrcode/"


def test_qrcode_form():
    data = {"url": "https://www.youtube.com/watch?v=nCEemcXzERk", "box_size": 10, "border": 2}
    response = client.post("/qrcode/form", data = data)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    response_body = b""
    for chunk in response.iter_content():
        response_body += chunk
    hash = hashlib.sha1(response_body).hexdigest()
    assert hash == "b7f494872858b727905fadc1137a8b3dea596ad9"
   

def test_qr():
    response = client.post("/qr")
    assert response.status_code == 302
    assert response.headers["location"] == "/qrcode/"


def test_qr_code():
    response = client.post("/qr-code")
    assert response.status_code == 302
    assert response.headers["location"] == "/qrcode/"




