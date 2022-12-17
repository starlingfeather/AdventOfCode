# Advent of code Year 2022 Day 2 tests
# Author = ambar
# Date = December 2022
import unittest
from advent import *


class TestAOC(unittest.TestCase):

    def test(self):
        example = """A Y
B X
C Z
"""
        answer = 15
        self.assertEqual(answer, solve_part_one(example))

        answer = 12
        self.assertEqual(answer, solve_part_two(example))


unittest.main()
