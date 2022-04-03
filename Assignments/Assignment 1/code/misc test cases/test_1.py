import unittest
from assignment1 import num_rad_sort

"""
    Test cases for Assignment 1 Task 1
    Author: Wei Hung 
"""

class Testing(unittest.TestCase):
    def test_1(self):
        nums = [7,5,3,6,4,1,9,2,10,8]
        expected_result = [1,2,3,4,5,6,7,8,9,10]
        for base in range(2, 100):
            result = num_rad_sort(nums, base)
            self.assertEqual(result, expected_result, 'Test 1 failed(' + str(base) + '), \nlist: '+ str(nums) + ' \nexpected result: ' + str(expected_result))        

    def test_2(self):
        nums = [40,10,71,31,98,39,100,78,13,80,48,43, 8,91,92, 2,28,46,77,65,12,57,21,64,72,55,58,49,81,68,42,37,27,59,25,76,66,63,29,34,50,47,41, 5,95,32,45, 1,74,15,69,67,93,96,44,90,75,82,86,60,23,56,54,53,94,51, 6,11,35,61, 4,62,89,73,20,87,97,70,19,24, 3,85, 7,79,18,22,17,99, 9,26,84,83,30,36,52,88,38,16,33,14]
        expected_result = list(range(1,101))
        for base in range(2, 100):
            result = num_rad_sort(nums, base)
            self.assertEqual(result, expected_result, 'Test 2 failed(' + str(base) + '), \nlist: '+ str(nums) + ' \nexpected result: ' + str(expected_result))        

    def test_3(self):
        nums = [0]
        expected_result = nums
        for base in range(2, 100):
            result = num_rad_sort(nums, base)
            self.assertEqual(result, expected_result, 'Test 3 failed(' + str(10) + '), \nlist: '+ str(nums) + ' \nexpected result: ' + str(expected_result))               
     
    def test_5(self):
        nums = [10,9,8,7,6,5,6,4,3,2,1,2,3]
        expected_result = [1,2,2,3,3,4,5,6,6,7,8,9,10]
        for base in range(2, 100):
            result = num_rad_sort(nums, base)
            self.assertEqual(result, expected_result, 'Test 5 failed(' + str(10) + '), \nlist: '+ str(nums) + ' \nexpected result: ' + str(expected_result))


if __name__ == '__main__':
    unittest.main()