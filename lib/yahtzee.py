

from enum import Enum, auto
import random

class Hand(Enum):
    ones = auto()
    twos = auto()
    threes = auto()
    fours = auto()
    fives = auto()
    sixes = auto()
    full_house = auto()
    chance = auto()

# Roll a die
#def roll_die():
#    retval = random.randint(1, 6)
#    return(retval)

# Roll 5 dice
#def roll_dice():
#    retval = []
#    for i in range(5):
#        retval.append(roll_die())
#    retval.sort()
#    return(retval)

class Score:

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
    # Figure out what posible hands we can have, and their score.
    #
    def score(self, dice):

        retval = {}

        data = self.analyze_dice(dice)

        if 1 in data["dice"]:
            retval[Hand.ones] = data["dice"][1] * 1

        if 2 in data["dice"]:
            retval[Hand.twos] = data["dice"][2] * 2

        if 3 in data["dice"]:
            retval[Hand.threes] = data["dice"][3] * 3

        if 4 in data["dice"]:
            retval[Hand.fours] = data["dice"][4] * 4

        if 5 in data["dice"]:
            retval[Hand.fives] = data["dice"][5] * 5

        if 6 in data["dice"]:
            retval[Hand.sixes] = data["dice"][6] * 6

        score = self.is_full_house(data["dice"])
        if score:
            retval[Hand.full_house] = 25

        # We always get Chance
        retval[Hand.chance]= sum(dice)
    
        return(retval)



