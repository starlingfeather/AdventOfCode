# Advent of code Year 2022 Day 3 tests
# Author = ambar
# Date = December 2022
import unittest
from advent import *


class TestAOC(unittest.TestCase):

    def test(self):
        example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
        answer = 157
        self.assertEqual(answer, solve_part_one(example))

        answer = 70
        self.assertEqual(answer, solve_part_two(example))

unittest.main()
