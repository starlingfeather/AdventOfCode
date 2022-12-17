# Advent of code Year 2022 Day 6 solution
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

    for i in range(4, len(data)):
        bite = data[i-4:i]
        if len(bite) == len(list(set(bite))):
            return i



def solve_part_two(data):
    for i in range(14, len(data)):
        bite = data[i-14:i]
        if len(bite) == len(list(set(bite))):
            return i


if __name__ == "__main__":
    runner.run(solve_part_one, solve_part_two, __file__)
