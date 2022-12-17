# Advent of code Year 2022 Day 6 tests
# Author = ambar
# Date = December 2022
import unittest
from advent import *


class TestAOC(unittest.TestCase):

    def test(self):
        self.assertEqual(7, solve_part_one("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
        self.assertEqual(5, solve_part_one("bvwbjplbgvbhsrlpgdmjqwftvncz"))
        self.assertEqual(6, solve_part_one("nppdvjthqldpwncqszvftbrmjlhg"))
        self.assertEqual(10, solve_part_one("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
        self.assertEqual(11, solve_part_one("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))

        self.assertEqual(19, solve_part_two("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
        self.assertEqual(23, solve_part_two("bvwbjplbgvbhsrlpgdmjqwftvncz"))
        self.assertEqual(23, solve_part_two("nppdvjthqldpwncqszvftbrmjlhg"))
        self.assertEqual(29, solve_part_two("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
        self.assertEqual(26, solve_part_two("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))
unittest.main()
