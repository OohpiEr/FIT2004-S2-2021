"""
Test cases for FIT2004 2021 S2 Assignment 1 Task 1.

Assumes num_rad_sort returns a new sorted copy instead of sorting in place.
Some minor modifications required for the test cases to work otherwise.
"""

import unittest

# If your code is stored in other files,
# change the import path below
from assignment1 import *


class TestNumRadixSort(unittest.TestCase):

    def test1(self):
        """ Provided example in assignment specs."""
        nums = [43, 101, 22, 27, 5, 50, 15]
        result = num_rad_sort(nums, 4)
        expected_result = [5, 15, 22, 27, 43, 50, 101]
        self.assertEqual(result, expected_result, msg=f'Cannot sort empty lists. Expected {expected_result}, got {result}.')

    
    def test3(self):
        """ Edge case: Largest element in list is 0.
        Author: Ci Leong
        """
        nums = [0, 0, 0]
        expected_result = nums
        result = num_rad_sort(nums, 10)
        self.assertEqual(result, expected_result, msg='Cannot sort lists with largest element 0.')
    
    def test4(self):
        """ Checks if base affects sort.
        Author: Ci Leong
        """
        nums = [43, 101, 22, 27, 5, 50, 15]
        expected_result = [5, 15, 22, 27, 43, 50, 101]
        for base in range(2, 1000):
            with self.subTest(base=base):
                result = num_rad_sort(nums, base)
                self.assertEqual(result, expected_result, msg=f"Doesn't work when base = {base}")


if __name__ == '__main__':
    unittest.main()