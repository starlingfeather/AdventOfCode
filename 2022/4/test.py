# Advent of code Year 2022 Day 4 tests
# Author = ambar
# Date = December 2022
import unittest
from code import *


class TestAOC(unittest.TestCase):
    def test(self):
        example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
        answer = 2
        self.assertEqual(answer, solve_part_one(example))

        answer = 4
        self.assertEqual(answer, solve_part_two(example))


unittest.main()
