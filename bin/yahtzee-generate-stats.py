#!/usr/bin/env python3
#
# This script creates all possible Yahtzee rolls
#


import sys
from pathlib import Path

# Add lib/ directory to sys.path
lib_dir = Path(__file__).resolve().parent.parent / "lib"
sys.path.insert(0, str(lib_dir))

from yahtzee import Hand, Score


#
# Get all our possible dice rolls.
#
def rolls():

    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1, 7):
                for d in range(1, 7):
                    for e in range(1, 7):
                        yield([a,b,c,d,e])


#
# Update our stats dictionary with the stats from a roll.
#
def update_stats(hand, stats, roll):

    score = hand.score(roll)
    for key, value in score.items():

        if not key in stats:
            stats[key] = {
                "count": 0,
                "total": 0,
                }

        stats[key]["count"] += 1
        stats[key]["total"] += value

    return(stats)


#
# Calculate additional stats
#
def calculate_stats(stats):

    for key, value in stats.items():
        stats[key]["average"] = round(
            (value["total"] / value["count"]), 2)
        stats[key]["percent"] = round(
            (value["count"] / 7776 * 100), 2)

    return(stats)


def main():

    hand = Hand()
    stats = {}

    # Perform all our dice rolls
    for roll in rolls():
        stats = update_stats(hand, stats, roll)

    # Now calculate additional stats
    stats = calculate_stats(stats)


#
# TODO:
# X score each roll
# X Save in stats
# X Calculate percent chance (7776 possible rolls)
# X Calculate average value
# 

main()

