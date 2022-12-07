# Advent of code Year 2022 Day 3 solution
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
    pri = 0
    for ruck in lines:
        pri += common_item(ruck)
    return pri


def common_item(ruck: str):

    first = ruck[slice(int(len(ruck) / 2))]
    second = ruck[slice(len(first), len(ruck))]

    print(f"first is {first} and ruck is {ruck}")

    item = list(set(first).intersection(set(second)))
    print(f"item is {item}")  # ['w']

    return priority(item)


def solve_part_two(data):
    lines = data.splitlines()
    pri = 0

    while lines:
        ruck1 = lines.pop(0)
        ruck2 = lines.pop(0)
        ruck3 = lines.pop(0)

        badge = set(ruck1).intersection(set(ruck2), set(ruck3))
        pri += priority(list(badge))

    return pri


def priority(item):
    item = item[0]
    if item.isupper():
        pri = ord(item) - 38
    else:
        pri = ord(item) - 96

    return pri


if __name__ == "__main__":
    runner.run(solve_part_one, solve_part_two, __file__)
