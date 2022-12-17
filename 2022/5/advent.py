# Advent of code Year 2022 Day 5 solution
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

    crates = data.split("\n\n")[0]
    instructions = data.split("\n\n")[1]
    numcrates = int(crates.split()[-1])  # pick off the last integer
    crates = crates.split("\n")  # break it into a list for each line
    pile = defaultdict(deque)

# set up the pile
    for layer in range(len(crates) - 1):  # [0, 1, 2], deliberately skip the numbered row
        for stack in range(numcrates):  # [0, 1, 2]
            if crates[layer][(stack * 4) + 1] != ' ':  # starting with 1, every 4th character is your crate
                pile[stack].appendleft(crates[layer][(stack * 4) + 1])
            # print(f'layer is {layer}, stack is {stack}, pile[stack] is {pile[stack]}')

# parse the instructions
    instrs = instructions.split("\n")
    for step in range(len(instrs)):
        move = list(aoc.extract_ints(instrs[step]))
        # print(f'move is {move}')
        num = move[0]
        src = move[1]-1
        dst = move[2]-1
        for i in range(num):
            pile[dst].append(pile[src].pop())

# assemble the string
    message = ''
    for i in range(len(pile)):
        message = message + pile[i].pop()

    return message


def solve_part_two(data):
    crates = data.split("\n\n")[0]
    instructions = data.split("\n\n")[1]
    numcrates = int(crates.split()[-1])  # pick off the last integer
    crates = crates.split("\n")  # break it into a list for each line
    pile = defaultdict(deque)

    # set up the pile
    for layer in range(len(crates) - 1):  # [0, 1, 2], deliberately skip the numbered row
        for stack in range(numcrates):  # [0, 1, 2]
            if crates[layer][(stack * 4) + 1] != ' ':  # starting with 1, every 4th character is your crate
                pile[stack].appendleft(crates[layer][(stack * 4) + 1])
            # print(f'layer is {layer}, stack is {stack}, pile[stack] is {pile[stack]}')

    # parse the instructions
    instrs = instructions.split("\n")
    for step in range(len(instrs)):
        move = list(aoc.extract_ints(instrs[step]))
        # print(f'move is {move}')
        num = move[0]
        src = move[1] - 1
        dst = move[2] - 1
        grab = deque()
        for i in range(num):
            grab.appendleft(pile[src].pop())
        # print(f'grab is {grab}')
        pile[dst].extend(grab)
        # print(f'pile[dst] is {pile[dst]}')

    # assemble the string
    message = ''
    for i in range(len(pile)):
        message = message + pile[i].pop()

    return message


if __name__ == "__main__":
    runner.run(solve_part_one, solve_part_two, __file__)
