
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app
from lib.yahtzee import Score, Hand

client = TestClient(app)


def test_yahtzee_class():

    score = Score()
    scores = score.score([1,2,3,4,5])
    assert scores[0]["hand"] == Hand.ones
    assert scores[0]["score"] == 1
    assert scores[1]["hand"] == Hand.twos
    assert scores[1]["score"] == 2
    assert scores[2]["hand"] == Hand.threes
    assert scores[2]["score"] == 3
    assert scores[3]["hand"] == Hand.fours
    assert scores[3]["score"] == 4
    assert scores[4]["hand"] == Hand.fives
    assert scores[4]["score"] == 5
    assert scores[len(scores) - 1]["hand"] == Hand.chance
    assert scores[len(scores) - 1]["score"] == 15

    scores = score.score([1,2,3,4,6])
    assert scores[4]["hand"] == Hand.sixes
    assert scores[4]["score"] == 6

    scores = score.score([1,2,2,2,3])
    assert scores[1]["hand"] == Hand.twos
    assert scores[1]["score"] == 6
    assert scores[len(scores) - 1]["hand"] == Hand.chance
    assert scores[len(scores) - 1]["score"] == 10

    scores = score.score([4,4,4,5,5])
    assert scores[0]["hand"] == Hand.fours
    assert scores[0]["score"] == 12

    scores = score.score([4,4,6,6,6])
    assert scores[0]["hand"] == Hand.fours
    assert scores[0]["score"] == 8

    scores = score.score([5,5,6,6,6])
    print("TEST", scores)
    assert scores[1]["hand"] == Hand.sixes
    assert scores[1]["score"] == 18
    assert scores[2]["hand"] == Hand.full_house
    assert scores[2]["score"] == 25


    # TODO:
    # Class: Score->score()
    # X test existing hands
    # - count_dice() - Add max and min
    # - count_dice() - Add unique dice
    # - count_dice() - Rename to analyize_dice()
    # - test all hands
    # - generation script: bin/generate-yahtzee-stats
    #   - data/yahtzee-stats.json
    #
    #assert response.status_code == 200
    #assert response.json()["source"]["ip"] == "testclient"
    #assert response.json()["verb"] == "GET"

