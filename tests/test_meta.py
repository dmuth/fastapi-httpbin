
import re

from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/version")
    
    assert response.status_code == 200
    assert re.match(r"^\d+\.\d+.\d+$", response.json()["version"])


