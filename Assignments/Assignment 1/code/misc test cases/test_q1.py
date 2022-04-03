""" Test cases for Question 1 of FIT2004 Assignment """

__author__ = "Arthur Lee"

import random
import unittest
from assignment1 import num_rad_sort


class TestNumRadSort(unittest.TestCase):
    BASES = [2, 4, 5, 8, 10, 15, 20, 40, 60, 100, 231, 324, 1343242, 2 * 10 ** 6 + (5 * 10 ** 5) * 9, 2 ** 22]

    def test1(self):
        """ Provided example in Assignment specification """
        nums = [43, 101, 22, 27, 5, 50, 15]
        expected = sorted(nums)
        for base in self.BASES:
            actual = num_rad_sort(nums, base)
            self.assertEqual(expected, actual, msg="Failed with Base " + str(base))

    def test2(self):
        """ Provided example in Lecture video """
        nums = [200, 151, 291, 981, 421, 671]
        expected = sorted(nums)
        for base in self.BASES:
            actual = num_rad_sort(nums, base)
            self.assertEqual(expected, actual, msg="Failed with Base " + str(base))

    def test3(self):
        """ Empty List """
        nums = []
        expected = sorted(nums)
        for base in self.BASES:
            actual = num_rad_sort(nums, base)
            self.assertEqual(expected, actual, msg="Failed with Base " + str(base))

    def test4(self):
        """ One item, only 0 """
        nums = [0]
        expected = sorted(nums)
        for base in self.BASES:
            actual = num_rad_sort(nums, base)
            self.assertEqual(expected, actual, msg="Failed with Base " + str(base))

    def test5(self):
        """ Multiple items, Max is 0 """
        nums = [0, 0, 0, 0, 0, 0]
        expected = sorted(nums)
        for base in self.BASES:
            actual = num_rad_sort(nums, base)
            self.assertEqual(expected, actual, msg="Failed with Base " + str(base))

    def test6(self):
        """ One large item """
        nums = [25234]
        expected = sorted(nums)
        for base in self.BASES:
            actual = num_rad_sort(nums, base)
            self.assertEqual(expected, actual, msg="Failed with Base " + str(base))

    def test7(self):
        """ All same value """
        nums = [69, 69, 69, 69, 69, 69, 69, 69, 69]
        expected = sorted(nums)
        for base in self.BASES:
            actual = num_rad_sort(nums, base)
            self.assertEqual(expected, actual, msg="Failed with Base " + str(base))

    def test8(self):
        """ Normal use """
        nums = [20, 9, 0, 1, 42, 69, 420, 2348023072, 4]
        expected = sorted(nums)
        for base in self.BASES:
            actual = num_rad_sort(nums, base)
            self.assertEqual(expected, actual, msg="Failed with Base " + str(base))

    def test9(self):
        """ Some same, some different """
        nums = [3, 1, 5, 3, 3, 3, 67, 2, 4, 132, 3, 3]
        expected = sorted(nums)
        for base in self.BASES:
            actual = num_rad_sort(nums, base)
            self.assertEqual(expected, actual, msg="Failed with Base " + str(base))

    def test10(self):
        """ Small random list """
        nums = [random.randint(0, 10000000000) for _ in range(251)]
        expected = sorted(nums)
        for base in self.BASES:
            actual = num_rad_sort(nums, base)
            self.assertEqual(expected, actual, msg="Failed with Base " + str(base))

    def test11(self):
        """ Medium random list """
        nums = [random.randint(0, 10000000000) for _ in range(1032)]
        expected = sorted(nums)
        for base in self.BASES:
            actual = num_rad_sort(nums, base)
            self.assertEqual(expected, actual, msg="Failed with Base " + str(base))

    def test12(self):
        """ Large random list """
        nums = [random.randint(0, 10000000000) for _ in range(15142)]
        expected = sorted(nums)
        for base in self.BASES:
            actual = num_rad_sort(nums, base)
            self.assertEqual(expected, actual, msg="Failed with Base " + str(base))


if __name__ == '__main__':
    unittest.main()
