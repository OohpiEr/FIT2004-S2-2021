"""
Test cases for FIT2004 2021 S2 Assignment 2 Task 1.
"""

import unittest
from assignment2 import count_encounters


class TestBestLampAllocation(unittest.TestCase):

    def test1(self):
        """ Provided example in assignment specs."""
        monster_list = [("bear", 5), ("imp", 2), ("kobold", 3), ("dragon", 10)]
        target_difficulty = 15
        result = count_encounters(target_difficulty, monster_list)
        expected_result = 9
        self.assertEqual(result, expected_result, msg=f'Cannot calculate all valid sets equal sum to target difficulty. Expected {expected_result}, got {result}.')

    def test2(self):
        """ Edge case: List is empty.
        """
        monster_list = []
        target_difficulty = 0
        result = count_encounters(target_difficulty, monster_list)
        expected_result = 1
        self.assertEqual(result, expected_result, msg=f'Cannot calculate valid set when monster list is empty. Expected {expected_result}, got {result}.')
    
    def test3(self):
        """ Monster with same difficulty 
        """
        monster_list = [("Naruto", 2), ("Naruto", 2), ("Naruto", 2), ("Sasuke", 1)]
        target_difficulty = 15
        result = count_encounters(target_difficulty, monster_list)
        expected_result = 120
        self.assertEqual(result, expected_result, msg=f'Cannot calculate all valid sets when same monster difficulty exist. Expected {expected_result}, got {result}.')
    
    def test4(self):
        """ No valid set exist equal to target difficulty
        """
        monster_list = [("PAIN", 9), ("Joker", 7), ("Darth Vader", 6), ("Thanos", 8), ("Voldemort", 5)]
        target_difficulty = 1
        result = count_encounters(target_difficulty, monster_list)
        expected_result = 0
        self.assertEqual(result, expected_result, msg=f'Cannot calculate when no valid set exist equal to target difficulty. Expected {expected_result}, got {result}.')

    def test5(self):
        """ Large target difficulty with small monster difficulty
        """
        monster_list = [("Raiden Shogun", 666), ("Ganyu", 66), ("Bennett", 1), ("Hu Tao", 10), ("Venti", 6),
                    ("Morax", 9), ("Kokomi", 13)]
        target_difficulty = 9999
        result = count_encounters(target_difficulty, monster_list)
        expected_result = 5615214837010
        self.assertEqual(result, expected_result, msg=f'Cannot calculate large target difficulty with small monster difficulty. Expected {expected_result}, got {result}.')

if __name__ == '__main__':
    unittest.main()