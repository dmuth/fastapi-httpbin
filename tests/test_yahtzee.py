
from fastapi.testclient import TestClient

from unittest.mock import AsyncMock

from main import app
from lib.yahtzee import Hand, Score

client = TestClient(app)


def test_yahtzee_class():

    hand = Hand()

    scores = hand.score([1,2,3,4,5])
    assert scores[Score.ones] == 1
    assert scores[Score.twos] == 2
    assert scores[Score.threes] == 3
    assert scores[Score.fours] == 4
    assert scores[Score.fives] == 5
    assert scores[Score.chance] == 15

    scores = hand.score([1,2,3,4,6])
    assert scores[Score.sixes] == 6

    scores = hand.score([1,2,2,2,3])
    assert scores[Score.twos] == 6
    assert scores[Score.three_of_a_kind] == 10
    assert scores[Score.chance] == 10

    scores = hand.score([4,4,4,5,5])
    assert scores[Score.fours] == 12
    assert scores[Score.three_of_a_kind] == 22
    assert scores[Score.full_house] == 25

    scores = hand.score([4,4,6,6,6])
    assert scores[Score.fours] == 8
    assert scores[Score.three_of_a_kind] == 26
    assert scores[Score.full_house] == 25

    scores = hand.score([1,1,1,2,2])
    assert scores[Score.ones] == 3
    assert scores[Score.twos] == 4
    assert scores[Score.three_of_a_kind] == 7
    assert scores[Score.full_house] == 25

    scores = hand.score([5,5,6,6,6])
    assert scores[Score.fives] == 10
    assert scores[Score.sixes] == 18
    assert scores[Score.three_of_a_kind] == 28
    assert scores[Score.full_house] == 25

    scores = hand.score([5,6,6,6,6])
    assert scores[Score.four_of_a_kind] == 29

    scores = hand.score([1,1,1,1,6])
    assert scores[Score.four_of_a_kind] == 10

    scores = hand.score([5,5,6,6,6])
    assert scores[Score.sixes] == 18
    assert scores[Score.three_of_a_kind] == 28
    assert scores[Score.full_house] == 25

    scores = hand.score([1,2,3,4,6])
    assert scores[Score.small_straight] == 30

    scores = hand.score([2,3,4,5,5])
    assert scores[Score.small_straight] == 30

    scores = hand.score([3,4,5,6,6])
    assert scores[Score.small_straight] == 30

    scores = hand.score([2,3,4,5,2])
    assert scores[Score.small_straight] == 30

    scores = hand.score([1,2,3,4,5])
    assert scores[Score.large_straight] == 40

    scores = hand.score([2,3,4,5,6])
    assert scores[Score.large_straight] == 40

    scores = hand.score([1,1,1,1,1])
    assert scores[Score.yahtzee] == 50

    scores = hand.score([4,4,4,4,4])
    assert scores[Score.yahtzee] == 50

    # TODO:
    # Class: Score->score()
    # X test existing hands
    # X count_dice() - Add max and min
    # X count_dice() - Add unique dice
    # X count_dice() - Rename to analyize_dice()
    # X turn value returned from array into dictionary
    # X test all hands
    # - generation script: bin/generate-yahtzee-stats
    #   - data/yahtzee-stats.json
    #
    #assert response.status_code == 200
    #assert response.json()["source"]["ip"] == "testclient"
    #assert response.json()["verb"] == "GET"

