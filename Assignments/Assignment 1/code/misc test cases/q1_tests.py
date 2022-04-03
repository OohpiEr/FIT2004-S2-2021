# %%
import unittest

import random

from assignment1 import num_rad_sort


class TestRadixSort(unittest.TestCase):

    def test_random(self):
        """ Checks 100 random lists containing random numbers (0 to 100,000) 
        of random sizes (1 to 10,000) of random bases (2 to 100,000)
        """
        lst_size = random.randint(1, 10000)
        for i in range(100):  # number of lists to check
            random_lst = []  # initialize random list as an empty list

            for j in range(lst_size):  # populate the list with random elements
                random_elem = random.randint(1, 100000)
                random_lst.append(random_elem)

            # random list has been built, test the list with a random base from 2 to 100,000
            # feel free to change the number of bases you want to test,
            # but beware that it is going to significantly impact runtime
            for k in range(1):
                random_base = random.randint(2, 100000)
                result_lst = num_rad_sort(random_lst, random_base)
                # use python's built-in sort function to check
                sorted_lst = sorted(random_lst)
                self.assertEqual(
                    result_lst, sorted_lst, f"For lst: {random_lst}, with base: {random_base}, result of radix sort was: {result_lst}, expected: {sorted_lst}")


if __name__ == '__main__':
    unittest.main()

# %%
