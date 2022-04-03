"""
I mutated the original list so if you did not, please change it TQ 
"""
from assignment1 import *
import unittest

class TestNumRadixSort(unittest.TestCase):

    """
    TASK 1
    """
    def test(self):
        """
        Description : Based on assignment specification and data
        """
        nums = [43, 101, 22, 27, 5, 50, 15]
        nums = num_rad_sort(nums, 10)
        expected_result = [5, 15, 22, 27, 43, 50, 101]
        self.assertEqual(nums, expected_result, "The output does not equal to the inbuilt sort function value (TEST)")

    
    def test2(self):
        """
        Description : Check for when everything is of equal element
        """
        nums = [2,2,2,2,2,2,2]
        expected_result = nums
        num_rad_sort(nums, 10)
        result = nums
        self.assertEqual(nums, expected_result, "The output does not equal to the inbuilt sort function value (TEST2)")
    
    def test3(self):
        """
        Description : Check if it's suitable to be use for bases from 2 - 1000
        """
        nums = [43, 101, 22, 27, 5, 50, 15]
        expected_result = [5, 15, 22, 27, 43, 50, 101]
        for base in range(2, 1000):
            with self.subTest(base=base):
                result = num_rad_sort(nums, base)
                self.assertEqual(result, expected_result, "The output does not equal to the inbuilt sort function value (TEST3)")

    """
    TASK 3 
    """

    def test5(self):
        """
        Description : Checking if radix_sort_string is working as intended
        """
        data = ["bcharacter","similar", "similar","as","ab","bchar","gabd","aa"]
        expected_result = sorted(data)
        radix_sort_str(data)
        self.assertEqual(data,expected_result, "The result for test 4 does not equal to the expected result (TEST4)")


if __name__ == '__main__':
    unittest.main()