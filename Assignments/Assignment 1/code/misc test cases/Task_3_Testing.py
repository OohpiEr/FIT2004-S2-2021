
from assignment1 import radix_sort_str
import unittest, string, random


def generate_random_string(length: int) -> str:
    return "".join(random.choices(string.ascii_lowercase + " ", k=length))


class TestRadixSortString(unittest.TestCase):
    def test_interest_groups(self):
        input_list = ["lol"]
        output_list = ["lol"]
        radix_sort_str(input_list)
        self.assertListEqual(input_list, output_list)

        input_list = ["abcaa", "a", "abc"]
        expected = sorted(input_list)
        radix_sort_str(input_list)
        self.assertListEqual(input_list, expected)

        input_list = ["fail", "gg", "nextsem", "next sem", "nextsem", "nextse", "broke", "sad", "dead"]
        expected = sorted(input_list)
        radix_sort_str(input_list)
        self.assertListEqual(input_list, expected)

        for i in range(168):
            random_strings = [generate_random_string(i) for _ in range(268)]
            expected_list = sorted(random_strings)
            radix_sort_str(random_strings)
            try:
                self.assertListEqual(random_strings, expected_list)
            except AssertionError:
                print(random_strings)
                print(expected_list)


if __name__ == "__main__":
    unittest.main()

