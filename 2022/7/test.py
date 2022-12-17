# Advent of code Year 2022 Day 7 tests
# Author = ambar
# Date = December 2022
import unittest
from advent import *


class TestAOC(unittest.TestCase):

    def test(self):
        example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
        answer = 95437
        self.assertEqual(answer, solve_part_one(example))


unittest.main()
