
import hashlib

from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)


def test_qrcode():
    response = client.post("/qrcode")
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
    assert response.headers["location"] == "/qrcode"


def test_qr_code():
    response = client.post("/qr-code")
    assert response.status_code == 302
    assert response.headers["location"] == "/qrcode"




