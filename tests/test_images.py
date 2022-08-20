
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)


def test_jpeg():
    response = client.get("/images/jpeg")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    
def test_png():
    response = client.get("/images/png")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    
def test_heic():
    response = client.get("/images/heic")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/heic"
    
def test_webp():
    response = client.get("/images/webp")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/webp"
    



