

from enum import Enum, auto
import random

class Hand(Enum):
    fives = auto()
    sixes = auto()
    full_house = auto()
    chance = auto()

# Roll a die
def roll_die():
    retval = random.randint(1, 6)
    return(retval)

# Roll 5 dice
def roll_dice():
    retval = []
    for i in range(5):
        retval.append(roll_die())
    retval.sort()
    return(retval)

#
# Count how many we have of each roll
# We can assume the sort are sorted.
#
def count_dice(dice):
    retval = {}

    for i in dice:
        if not i in retval:
            retval[i] = 0
        retval[i] += 1

    return(retval)

def is_full_house(counts):

    retval = 0
    
    three = 0
    two = 0

    for key, value in counts.items():
        if value == 3:
            three = key * value
        if value == 2:
            two = key * value

    if two and three:
        retval = two + three
        
    return(retval)
    

#
# Figure out what posible hands we can have, and their score.
#
def classify(dice):

    retval = []

    counts = count_dice(dice)

    if 5 in counts:
        retval.append({"hand": Hand.fives, "score": counts[5]* 5})
    if 6 in counts:
        retval.append({"hand": Hand.sixes, "score": counts[6]* 6})

    score = is_full_house(counts)
    if score:
        retval.append({"hand": Hand.full_house, "score": score})

    
    # We always get Chance
    retval.append({"hand": Hand.chance, "score": sum(dice)})


    
    return(retval)

dice = roll_dice()
print(classify([1,2,3,4,5]))
print(classify([1,2,3,4,6]))
print(classify([1,1,2,2,3]))
print(classify([4,4,4,5,5]))
print(classify([5,5,5,6,6]))
print(classify([4,4,6,6,6]))
print(classify([5,5,6,6,6]))


print(classify(dice))


