
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

#from .main import app
from main import app

client = TestClient(app)

def test_read_main():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == { "Hello": "World"}

def test_get_get():
	response = client.get("/get")
	assert response.status_code == 200
	assert response.json()["source"]["ip"] == "testclient"
	assert response.json()["headers"]["host"] == "testserver"




