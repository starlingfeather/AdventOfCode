# Advent of code Year 2022 Day 5 tests
# Author = ambar
# Date = December 2022
import unittest
from advent import *


class TestAOC(unittest.TestCase):
    def test(self):
        example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

        answer = "CMZ"
        self.assertEqual(answer, solve_part_one(example))

        answer = "MCD"
        self.assertEqual(answer, solve_part_two(example))

unittest.main()
