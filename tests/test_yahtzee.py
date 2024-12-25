
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app
from lib.yahtzee import Hand

client = TestClient(app)

def test_yahtzee_class():

    pass
    # TODO:
    # - flesh out tests
    # - generation script: bin/generate-yahtzee-stats
    #   - data/yahtzee-stats.json
    #
    #assert response.status_code == 200
    #assert response.json()["source"]["ip"] == "testclient"
    #assert response.json()["verb"] == "GET"


