
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)


def test_html():
    response = client.get("/html")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    
def test_json():
    response = client.get("/json")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["title"] == "Undertale Soundtrack"
    
def test_robots_txt():
    response = client.get("/robots.txt")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/plain; charset=utf-8"

def test_deny():
    response = client.get("/deny")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
    assert "You pet the Dog." in response.text

def test_xml():
    response = client.get("/xml")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/xml "
    assert "<track>Hopes and Dreams</track>" in response.text

def test_utf8():
    response = client.get("/encoding/utf8")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
    assert "∮ E⋅da = Q" in response.text



