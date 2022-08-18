
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


def test_response_headers():

    headers = {}
    response = client.get("/response-headers", params = headers)
    assert response.status_code == 200
    assert response.json()["message"] == "0 headers set in response"
    

    headers = {"headers": ["x-cheetah-sound:chirp"]}
    response = client.get("/response-headers", params = headers)
    assert response.status_code == 200
    assert "x-cheetah-sound" in response.headers
    assert response.json()["message"] == "1 headers set in response"

    headers = {"headers": ["x-cheetah-sound:chirp", "x-goat-sound:bleat"]}
    response = client.get("/response-headers", params = headers)
    assert response.status_code == 200
    assert "x-cheetah-sound" in response.headers
    assert "x-goat-sound" in response.headers
    assert response.json()["message"] == "2 headers set in response"

    headers = {"headers": ["x-this-should-fail"]}
    response = client.get("/response-headers", params = headers)
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "value_error.str.format"

    headers = {"headers": ["x-this:should:fail"]}
    response = client.get("/response-headers", params = headers)
    assert response.status_code == 422
    assert response.json()["detail"]["type"] == "value_error.str.format"



