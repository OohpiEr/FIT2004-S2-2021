""" Test cases for Question 1 of FIT2004 Assignment 2 """

__author__ = "Arthur Lee"

import unittest
import random
from assignment2 import count_encounters


class TestCountEncounters(unittest.TestCase):
    def test1(self):
        """ Provided Example in Assignment Spec """
        target_difficulty = 15
        monster_list = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]
        actual = count_encounters(target_difficulty, monster_list)
        expected = 9
        self.assertEqual(expected, actual)

    def test2(self):
        """ Empty Monster List and Zero Difficulty """
        target_difficulty = 0
        monster_list = []
        actual = count_encounters(target_difficulty, monster_list)
        expected = 1
        self.assertEqual(expected, actual)

    def test3(self):
        """ Empty Monster List and High Difficulty """
        target_difficulty = 2343252
        monster_list = []
        actual = count_encounters(target_difficulty, monster_list)
        expected = 0
        self.assertEqual(expected, actual)

    def test4(self):
        """ Monster with Same Difficulty and Different Name Present """
        target_difficulty = 18
        monster_list = [("Zhongli", 6), ("Morax", 6), ("Rex Lapis", 6), ("Diluc", 5)]
        actual = count_encounters(target_difficulty, monster_list)
        expected = 10
        self.assertEqual(expected, actual)

    def test5(self):
        """ Monster with Same Difficulty and Same Name Present """
        target_difficulty = 16
        monster_list = [("Genshin", 4), ("Genshin", 4), ("Genshin", 4), ("Mihoyo", 11), ("Genshin", 4)]
        actual = count_encounters(target_difficulty, monster_list)
        expected = 35
        self.assertEqual(expected, actual)

    def test6(self):
        """ Monster with Different Difficulty and Same Name Present """
        target_difficulty = 6
        monster_list = [("Monke", 5), ("Thanos", 2), ("Thanos", 3)]
        actual = count_encounters(target_difficulty, monster_list)
        expected = 2
        self.assertEqual(expected, actual)

    def test7(self):
        """ No valid Combination """
        target_difficulty = 12
        monster_list = [("FIT2014", 9), ("FIT1008", 5), ("FIT2004", 8), ("FIT3155", 15)]
        actual = count_encounters(target_difficulty, monster_list)
        expected = 0
        self.assertEqual(expected, actual)

    def test8(self):
        """ Zero Difficulty and Large Monster List """
        target_difficulty = 0
        monster_list = [("Iron Man", 324), ("Thor", 1432), ("Captain America", 23), ("Hulk", 2354)]
        actual = count_encounters(target_difficulty, monster_list)
        expected = 1
        self.assertEqual(expected, actual)

    def test9(self):
        """ Small Random Case """
        target_difficulty = 100
        monster_list = [("0", 12)]
        for i in range(24):
            random.seed(i)
            monster_list.append((str(i), random.randint(1, 100)))
        result = count_encounters(target_difficulty, monster_list)
        print()
        print("Q1 Small Random Case: " + str(result))

    def test10(self):
        """ Medium Random Case """
        target_difficulty = 1000
        monster_list = [("0", 9)]
        for i in range(499):
            random.seed(i - 10000)
            monster_list.append((str(i), random.randint(1, 1000)))
        result = count_encounters(target_difficulty, monster_list)
        print()
        print("Q1 Medium Random Case: " + str(result))

    def test11(self):
        """ Large Random Case """
        target_difficulty = 10000
        monster_list = [("0", 345)]
        for i in range(4999):
            random.seed(i * 47)
            monster_list.append((str(i), random.randint(1, 10000)))
        result = count_encounters(target_difficulty, monster_list)
        print()
        print("Q1 Large Random Case: " + str(result))


if __name__ == '__main__':
    unittest.main()
