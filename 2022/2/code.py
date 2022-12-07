# Advent of code Year 2022 Day 2 solution
# Author = ambar
# Date = December 2022
import runner
import aocutil as aoc
import bisect
from collections import *
from copy import deepcopy
from dataclasses import dataclass
from functools import cache, lru_cache, reduce
import itertools as it
import math
from multiset import Multiset
import numpy as np
import operator
from pprint import pprint
import re

rock = 1
paper = 2
scissors = 3
win = 6
draw = 3
lose = 0

shape_table = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
anticipate_table = {"X": lose, "Y": draw, "Z": win}


def solve_part_one(data):
    aoc.guess_input(data)
    lines = data.splitlines()
    total = 0
    for line in lines:
        print(f"line is {line}")
        total += score(line)
        print(f"total is {total}")
    return total


def solve_part_two(data):  # 'A Z'
    total = 0
    lines = data.splitlines()
    for line in lines:
        print(f"line is {line}")
        my_move = anticipate(line)
        my_score = score(my_move)
        print(f"my move is {my_move} and my score is {my_score}")
        total += my_score
    return total


def anticipate(round: str):
    them: str = round[0]
    their_shape: int = shape_table[them]
    play: str = round[slice(2)]

    desired_outcome: int = anticipate_table[round[2]]

    if desired_outcome == draw:
        play += them
    elif desired_outcome == win:
        if their_shape == rock:
            play += "Y"
        elif their_shape == paper:
            play += "Z"
        else:
            play += "X"
    else:
        if their_shape == rock:
            play += "Z"
        elif their_shape == paper:
            play += "X"
        else:
            play += "Y"

    return play


def score(round):  # 'A Z'
    me = round[2]
    my_shape_score = shape_table[me]
    print(f"my_shape_score is {my_shape_score}")

    my_outcome_score = outcome(round)
    print(f"my outcome score is {my_outcome_score}")

    return my_shape_score + my_outcome_score


def outcome(round):
    me = shape_table[round[2]]
    them = shape_table[round[0]]

    if me == them:
        return draw
    elif me == rock and them == scissors:
        return win
    elif me == scissors and them == paper:
        return win
    elif me == paper and them == rock:
        return win
    else:
        return lose


if __name__ == "__main__":
    runner.run(solve_part_one, solve_part_two, __file__)
