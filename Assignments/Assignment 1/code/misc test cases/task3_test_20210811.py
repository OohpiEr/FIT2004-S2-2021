"""
Test cases for FIT2004 2021 S2 Assignment 1 Task 1.

Assumes radix_sort_str (or whatever you call it) returns a new sorted copy
instead of sorting in place. Some minor modifications are required for
the test cases to work otherwise.
"""

import unittest

# If your code is stored in other files,
# change the import path below
from assignment1 import *


# If your radix sort for strings function is not named
# radix_sort_str, uncomment the line below and set the
# r-value to the name of the function for it to work.
# This unifies the name of the radix sort function below.

# radix_sort_str = 


class TestStrRadixSort(unittest.TestCase):

    def test1(self):
        """ Edge case: List is empty.
        Author: Ci Leong
        """
        arr = []
        result = radix_sort_str(arr)
        self.assertEqual(result, [], msg=f'Cannot sort empty lists. Expected [], got {result}.')

    def test2(self):
        """ Tests whether strings are sorted lexicographically.
        Failure of this test could mean strings are sorted by numerical value.
        Or... it could be processed in other orders as well (might not even be ordered LOL).
        Author: Ci Leong
        """
        arr1 = ['ab', 'c']
        arr2 = ['c', 'ab']
        result1 = radix_sort_str(arr1)
        result2 = radix_sort_str(arr2)
        expected_result = ['ab', 'c']
        self.assertTrue(result1 == result2 == expected_result,
        msg=f'Strings are not sorted lexicographically or unsorted. Expected {expected_result}, got {result1} and {result2} (both must be correct)')

    def test3(self):
        """ Tests if ' ' and '' are wrongly placed in 'a''s bin.
        Failing this test case probably means there is no separated bins for '' and ' '.
        Author: Ci Leong
        """
        arr = [' ', '']
        result = radix_sort_str(arr)
        expected_result = ['', ' ']
        self.assertEqual(result, expected_result, msg=f'Expected {expected_result}, got {result}.')

        arr = ['a', '']
        result = radix_sort_str(arr)
        expected_result = ['', 'a']
        self.assertEqual(result, expected_result, msg=f'Expected {expected_result}, got {result}.')


class TestInterestGroups(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        pass
        

if __name__ == '__main__':
    unittest.main()