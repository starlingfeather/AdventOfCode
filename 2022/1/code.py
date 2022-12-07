# Advent of code Year 2022 Day 1 solution
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
    content = data.splitlines()

    elf = 0
    inventory = []
    inventory.append(0)

    for line in content:
        if line == '':
            # print(f'Finished elf {elf}')
            elf = elf + 1
            inventory.append(0)
        else:
            inventory[elf] += int(line)
            # print(f'Elf {elf} has inventory {inventory[elf]}')
            
    inventory.sort(reverse=True)
    return inventory[0]


def solve_part_two(data):
    content = data.splitlines()

    elf = 0
    inventory = []
    inventory.append(0)

    for line in content:
        if line == '':
            # print(f'Finished elf {elf}')
            elf = elf + 1
            inventory.append(0)
        else:
            inventory[elf] += int(line)
            # print(f'Elf {elf} has inventory {inventory[elf]}')

    inventory.sort(reverse=True)
    return inventory[0] + inventory[1] + inventory[2]

if __name__ == "__main__":
    runner.run(solve_part_one, solve_part_two, __file__)
