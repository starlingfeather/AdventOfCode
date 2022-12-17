# Advent of code Year 2022 Day 1 tests
# Author = ambar
# Date = December 2022
import unittest
from advent import *


class TestAOC(unittest.TestCase):

    def test(self):
        example = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
        answer = 24000
        self.assertEqual(answer, solve_part_one(example))

        answer = 45000
        self.assertEqual(answer, solve_part_two(example))


unittest.main()
