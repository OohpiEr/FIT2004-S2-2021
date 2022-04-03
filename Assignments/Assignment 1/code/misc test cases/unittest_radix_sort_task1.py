
import unittest, random
from radix_sort import radix_sort
from typing import List


class TestRadixSort(unittest.TestCase):
    def test_radix_sort(self):
        input_list = []
        base_list = [90, 10, 7, 4]
        for base in base_list:
            radix_sort(input_list, base)
            self.assertListEqual(input_list, [])

        input_list = [18]
        output_list = [18]
        for base in base_list:
            radix_sort(input_list, base)
            self.assertListEqual(input_list, output_list)

        base_list = [90, 10, 7, 4]
        input_list = [0 for _ in range(20)]
        for base in base_list:
            radix_sort(input_list, base)
            self.assertListEqual(input_list, input_list)

        base_list = [x for x in range(2, 102)]
        input_list = [43, 101, 22, 27, 5, 50, 15]
        output_list = [5, 15, 22, 27, 43, 50, 101]
        for base in base_list:
            radix_sort(input_list, base)
            self.assertListEqual(input_list, output_list)

        input_list = [random.randint(0, 238472323) for _ in range(250000)]
        for base in base_list:
            radix_sort(input_list, base)
            self.assertTrue(self.__is_sorted_aux(input_list))

    def __is_sorted_aux(self, a_list: List[int]) -> bool:
        for i in range(len(a_list) - 1):
            if a_list[i] > a_list[i + 1]:
                return False
        return True


if __name__ == "main":
    unittest.main()

