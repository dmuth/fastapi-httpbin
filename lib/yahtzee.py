

from enum import Enum, auto
import random

class Score(Enum):
    ones = auto()
    twos = auto()
    threes = auto()
    fours = auto()
    fives = auto()
    sixes = auto()

    three_of_a_kind = auto()
    four_of_a_kind = auto()
    full_house = auto()
    small_straight = auto()
    large_straight = auto()
    yahtzee = auto()

    chance = auto()


class Hand:

    stats = {}

    def __init__(self, stats):
        self.stats = stats


    #
    # Count how many we have of each roll
    #
    def analyze_dice(self, dice):

        retval = {
            "max": None,
            "min": None,
            "span": None,
            "num_unique": None,
            "dice": {}
            }

        dice.sort()

        # Get unique dice counts
        for i in dice:
            if not i in retval["dice"]:
                retval["dice"][i] = 0
            retval["dice"][i] += 1

        retval["max"] = max(dice)
        retval["min"] = min(dice)
        retval["span"] = retval["max"] - retval["min"]
        retval["num_unique"] = len(set(dice))

        return(retval)


    def is_three_of_a_kind(self, counts):

        retval = False

        for key, value in counts.items():
            if value == 3:
                return(True)


    def is_four_of_a_kind(self, counts):

        retval = False

        for key, value in counts.items():
            if value == 4:
                return(True)


    #
    # Is this hand full house?
    #
    def is_full_house(self, counts):

        retval = False
    
        three = 0
        two = 0

        for key, value in counts.items():
            if value == 3:
                three = key * value
            if value == 2:
                two = key * value

        if two and three:
            retval = True
        
        return(retval)
    

    #
    # Is this a small straight?  Since we only have three
    # possibilities, it just makes sense to hard code them.
    #
    def is_small_straight(self, data):

        dice = data["dice"]

        if 1 in dice and 2 in dice and 3 in dice and 4 in dice:
            return(True)

        if 2 in dice and 3 in dice and 4 in dice and 5 in dice:
            return(True)

        if 3 in dice and 4 in dice and 5 in dice and 6 in dice:
            return(True)

        return(False)

    #
    # Is this a large straight?  We only have two 
    # possibilities to check for.
    #
    def is_large_straight(self, data):
        dice = data["dice"]

        if 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
            return(True)

        if 2 in dice and 3 in dice and 4 in dice and 5 in dice and 6 in dice:
            return(True)

        return(False)

    def is_yahtzee(self, data):

        if data["num_unique"] == 1:
            return(True)

        return(False)


    #
    # Figure out what posible hands we can have, and their score.
    #
    def score(self, dice):

        retval = {}

        data = self.analyze_dice(dice)

        if 1 in data["dice"]:
            retval[Score.ones] = {"score": data["dice"][1] * 1 }

        if 2 in data["dice"]:
            retval[Score.twos] = {"score": data["dice"][2] * 2 }

        if 3 in data["dice"]:
            retval[Score.threes] = {"score": data["dice"][3] * 3 }

        if 4 in data["dice"]:
            retval[Score.fours] = {"score": data["dice"][4] * 4 }

        if 5 in data["dice"]:
            retval[Score.fives] = {"score": data["dice"][5] * 5 }

        if 6 in data["dice"]:
            retval[Score.sixes] = {"score": data["dice"][6] * 6 }

        if self.is_three_of_a_kind(data["dice"]):
            retval[Score.three_of_a_kind] = {"score": sum(dice) }

        if self.is_four_of_a_kind(data["dice"]):
            retval[Score.four_of_a_kind] = {"score": sum(dice) }

        if self.is_full_house(data["dice"]):
            retval[Score.full_house] = {"score": 25 }

        if self.is_small_straight(data):
            retval[Score.small_straight] = {"score": 30 }

        if self.is_large_straight(data):
            retval[Score.large_straight] = {"score": 40 }

        if self.is_yahtzee(data):
            retval[Score.yahtzee] = {"score": 50 }

        # We always get Chance
        retval[Score.chance]= {"score": sum(dice) }
    
        for key, value in retval.items():
            retval[key]["average"] = self.stats[key]["average"]
            retval[key]["percent"] = self.stats[key]["percent"]

        return(retval)



