
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app
from lib.yahtzee import Score, Hand

client = TestClient(app)


def test_yahtzee_class():

    score = Score()
    scores = score.score([1,2,3,4,5])
    assert scores[Hand.ones] == 1
    assert scores[Hand.twos] == 2
    assert scores[Hand.threes] == 3
    assert scores[Hand.fours] == 4
    assert scores[Hand.fives] == 5
    assert scores[Hand.chance] == 15

    scores = score.score([1,2,3,4,6])
    assert scores[Hand.sixes] == 6

    scores = score.score([1,2,2,2,3])
    assert scores[Hand.twos] == 6
    assert scores[Hand.chance] == 10

    scores = score.score([4,4,4,5,5])
    assert scores[Hand.fours] == 12

    scores = score.score([4,4,6,6,6])
    assert scores[Hand.fours] == 8

    scores = score.score([1,1,1,2,2])
    print("TEST", scores)

    return
    scores = score.score([5,5,6,6,6])
    print("TEST", scores)

    scores = score.score([5,6,6,6,6])
    print("TEST", scores)

    scores = score.score([1,1,1,1,6])
    print("TEST", scores)

    scores = score.score([5,5,6,6,6])
    print("TEST", scores)
    assert scores[Hand.sixes] == 18
    assert scores[Hand.full_house] == 25

    scores = score.score([1,2,3,4,6])
    print("TEST", scores)

    scores = score.score([2,3,4,5,2])
    print("TEST", scores)

    scores = score.score([1,2,3,4,5])
    print("TEST", scores)

    scores = score.score([2,3,4,5,6])
    print("TEST", scores)

    scores = score.score([1,1,1,1,1])
    print("TEST", scores)

    scores = score.score([4,4,4,4,4])
    print("TEST", scores)

    # TODO:
    # Class: Score->score()
    # X test existing hands
    # X count_dice() - Add max and min
    # X count_dice() - Add unique dice
    # X count_dice() - Rename to analyize_dice()
    # - turn value returned from array into dictionary
    # - test all hands
    # - generation script: bin/generate-yahtzee-stats
    #   - data/yahtzee-stats.json
    #
    #assert response.status_code == 200
    #assert response.json()["source"]["ip"] == "testclient"
    #assert response.json()["verb"] == "GET"

