#!/usr/bin/env python3
#
# This script creates all possible Yahtzee rolls
#

from enum import Enum
import json
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


#
# Write our stats out to a file.
#
def write_file(stats, filename):

    # The key name is an enum, so we need to stringify that.
    stats_string = { key.name: value for key, value in stats.items() }

    with open(filename, "w") as file:
        json.dump(stats_string, file, indent = 4)


#
# Read our file and turn keys back into Enums
#
def read_file(filename):

    with open(filename, "r") as file:
        stats = json.load(file)

    stats = {Score[key]: value for key, value in stats.items()}

    return(stats)


def main():

    hand = Hand()
    stats = {}

    filename = "data/yahtzee-stats.json"

    # Perform all our dice rolls
    for roll in rolls():
        stats = update_stats(hand, stats, roll)

    stats = calculate_stats(stats)

    write_file(stats, filename)

    # 
    # Now read our file back in and turn the key back 
    # into an enum.  This is mostly for proof of concept purposes
    # as I am writing this, with this code to be later integrated
    # into the FastAPI app.
    #
    stats = read_file(filename)


main()

