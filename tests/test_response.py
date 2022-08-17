
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)


def test_cache():
    response = client.get("/cache")
    assert response.status_code == 200
    
    headers = {"If-Modified-Since": "12345"}
    response = client.get("/cache", headers = headers)
    assert response.status_code == 304

    headers = {"If-None-Match": "67890"}
    response = client.get("/cache", headers = headers)
    assert response.status_code == 304

    headers = {"If-Modified-Since": "12345", "If-None-Match": "67890"}
    response = client.get("/cache", headers = headers)
    assert response.status_code == 304


def test_cache_seconds():
    response = client.get("/cache/12345")
    assert response.status_code == 200
    assert response.headers["cache-control"] == "public, max-age=12345"


def test_etag():
    response = client.get("/etag/12345")
    assert response.status_code == 200
    assert response.headers["etag"] == "12345"

    headers = {"If-None-Match": "12345"}
    response = client.get("/etag/12345", headers = headers)
    assert response.status_code == 304

    headers = {"If-None-Match": "67890"}
    response = client.get("/etag/12345", headers = headers)
    assert response.status_code == 200

    headers = {"If-Match": "12345"}
    response = client.get("/etag/12345", headers = headers)
    assert response.status_code == 200

    headers = {"If-Match": "67890"}
    response = client.get("/etag/12345", headers = headers)
    assert response.status_code == 412

    #
    # According to https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match,
    # If-None-Match has precedence here.
    #
    headers = {"If-None-Match": "12345", "If-Match": "12345"}
    response = client.get("/etag/12345", headers = headers)
    assert response.status_code == 304

    headers = {"If-None-Match": "67890", "If-Match": "12345"}
    response = client.get("/etag/12345", headers = headers)
    assert response.status_code == 200


# TODO:
# /response-headers - Set headers with "headers" array for GET and POST
# Set possible HTTP codes that can be returned and see if that shows up in the docs

