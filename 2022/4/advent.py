# Advent of code Year 2022 Day 4 solution
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


def solve_part_one(data):
    aoc.guess_input(data)
    lines = data.splitlines()
    subsets = 0
    for line in lines:
        spread = line.partition(",")
        seta = range_to_set(spread[0].partition("-"))
        setb = range_to_set(spread[2].partition("-"))
        # print(f'A is {seta}\nB is {setb}')
        if (seta <= setb) or (setb <= seta):
            subsets += 1
    return subsets


def range_to_set(raange):
    return set(range(int(raange[0]), int(raange[2]) + 1))


def solve_part_two(data):
    lines = data.splitlines()
    overlaps = 0
    for line in lines:
        spread = line.partition(",")
        seta = range_to_set(spread[0].partition("-"))
        setb = range_to_set(spread[2].partition("-"))
        # print(f"A is {seta}\nB is {setb}")
        if not seta.isdisjoint(setb):
            overlaps += 1

    return overlaps


if __name__ == "__main__":
    runner.run(solve_part_one, solve_part_two, __file__)
