
import json

from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

from . import decode_qrcode

client = TestClient(app)


def test_qrcode_post():

    url = "https://www.youtube.com/watch?v=nCEemcXzERk"

    response = client.post("/qrcode/json")
    assert response.status_code == 422

    data = {"url": url, "box_size": 10, "border": 4}
    response = client.post("/qrcode/json", json = data)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    response_body = b""
    for chunk in response.iter_bytes():
        response_body += chunk

    uuid_decoded = decode_qrcode(response_body)
    assert uuid_decoded == url

    data = {"url": url, "box_size": 10, "border": 4, "transparent_background": True}
    response = client.post("/qrcode/json", json = data)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    response_body = b""
    for chunk in response.iter_bytes():
        response_body += chunk

    uuid_decoded = decode_qrcode(response_body)
    assert uuid_decoded == url

    # Test small border
    data = {"url": url, "box_size": 10, "border": 2}
    response = client.post("/qrcode/json", json = data)
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "value_error.int.min_size"


def test_qrcode_post_size():

    url = "1234567890"

    data = {"url": url, "box_size": 10, "border": 4}
    response = client.post("/qrcode/json", json = data)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    response_body = b""
    for chunk in response.iter_bytes():
        response_body += chunk

    uuid_decoded = decode_qrcode(response_body)
    assert uuid_decoded == url

    url = "1234"

    data = {"url": url, "box_size": 10, "border": 4}
    response = client.post("/qrcode/json", json = data)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    response_body = b""
    for chunk in response.iter_bytes():
        response_body += chunk

    uuid_decoded = decode_qrcode(response_body)
    assert uuid_decoded == url


def test_qrcode_get():
    response = client.get("/qrcode", allow_redirects = False)
    assert response.status_code == 302
    assert response.headers["location"] == "/qrcode/"


def test_qrcode_form():

    url = "https://www.youtube.com/watch?v=nCEemcXzERk"

    data = {"url": url, "box_size": 10, "border": 4}
    response = client.post("/qrcode/form", data = data)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    response_body = b""
    for chunk in response.iter_bytes():
        response_body += chunk

    uuid_decoded = decode_qrcode(response_body)
    assert uuid_decoded == url

    data = {"url": url, "box_size": 10, "border": 4, "transparent_background": True}
    response = client.post("/qrcode/form", data = data)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    response_body = b""
    for chunk in response.iter_bytes():
        response_body += chunk

    uuid_decoded = decode_qrcode(response_body)
    assert uuid_decoded == url

    data = {"url": url, "box_size": 10, "border": 2}
    response = client.post("/qrcode/form", data = data)
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "value_error.int.min_size"


#def test_qr():
#    response = client.post("/qr")
#    assert response.status_code == 302
#    assert response.headers["location"] == "/qrcode/"


#def test_qr_code():
#    response = client.post("/qr-code")
#    assert response.status_code == 302
#    assert response.headers["location"] == "/qrcode/"




