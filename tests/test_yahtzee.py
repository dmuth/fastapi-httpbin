
import json
from unittest.mock import AsyncMock

from fastapi.testclient import TestClient


from main import app
from lib.yahtzee import Hand, Score

client = TestClient(app)


def load_stats():

    filename = "data/yahtzee-stats.json"

    with open(filename, "r") as file:
        stats = json.load(file)

    stats = {Score[key]: value for key, value in stats.items()}

    return(stats)


def test_yahtzee_class():

    stats = load_stats()

    hand = Hand(stats)

    scores = hand.score([1,2,3,4,5])
    assert scores[Score.ones]["score"] == 1
    assert scores[Score.ones]["average"] == 1.39
    assert scores[Score.ones]["percent"] == 59.81
    assert scores[Score.twos]["score"] == 2
    assert scores[Score.threes]["score"] == 3
    assert scores[Score.fours]["score"] == 4
    assert scores[Score.fives]["score"] == 5
    assert scores[Score.chance]["score"] == 15

    scores = hand.score([1,2,3,4,6])
    assert scores[Score.sixes]["score"] == 6

    scores = hand.score([1,2,2,2,3])
    assert scores[Score.twos]["score"] == 6
    assert scores[Score.three_of_a_kind]["score"] == 10
    assert scores[Score.chance]["score"] == 10

    scores = hand.score([4,4,4,5,5])
    assert scores[Score.fours]["score"] == 12
    assert scores[Score.three_of_a_kind]["score"] == 22
    assert scores[Score.full_house]["score"] == 25

    scores = hand.score([4,4,6,6,6])
    assert scores[Score.fours]["score"] == 8
    assert scores[Score.three_of_a_kind]["score"] == 26
    assert scores[Score.full_house]["score"] == 25

    scores = hand.score([1,1,1,2,2])
    assert scores[Score.ones]["score"] == 3
    assert scores[Score.twos]["score"] == 4
    assert scores[Score.three_of_a_kind]["score"] == 7
    assert scores[Score.full_house]["score"] == 25

    scores = hand.score([5,5,6,6,6])
    assert scores[Score.fives]["score"] == 10
    assert scores[Score.sixes]["score"] == 18
    assert scores[Score.three_of_a_kind]["score"] == 28
    assert scores[Score.full_house]["score"] == 25

    scores = hand.score([5,6,6,6,6])
    assert scores[Score.four_of_a_kind]["score"] == 29

    scores = hand.score([1,1,1,1,6])
    assert scores[Score.four_of_a_kind]["score"] == 10

    scores = hand.score([5,5,6,6,6])
    assert scores[Score.sixes]["score"] == 18
    assert scores[Score.three_of_a_kind]["score"] == 28
    assert scores[Score.full_house]["score"] == 25

    scores = hand.score([1,2,3,4,6])
    assert scores[Score.small_straight]["score"] == 30

    scores = hand.score([2,3,4,5,5])
    assert scores[Score.small_straight]["score"] == 30

    scores = hand.score([3,4,5,6,6])
    assert scores[Score.small_straight]["score"] == 30

    scores = hand.score([2,3,4,5,2])
    assert scores[Score.small_straight]["score"] == 30

    scores = hand.score([1,2,3,4,5])
    assert scores[Score.large_straight]["score"] == 40

    scores = hand.score([2,3,4,5,6])
    assert scores[Score.large_straight]["score"] == 40

    scores = hand.score([1,1,1,1,1])
    assert scores[Score.yahtzee]["score"] == 50

    scores = hand.score([4,4,4,4,4])
    assert scores[Score.yahtzee]["score"] == 50

    # TODO:
    #
    #assert response.status_code == 200
    #assert response.json()["source"]["ip"] == "testclient"
    #assert response.json()["verb"] == "GET"

