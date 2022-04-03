""" Unit tests for Task 1 of FIT2004 Assignment 3 """

__author__ = "Arthur Lee"

import unittest
import string
import random
from task1 import lex_pos

# %%
def inefficient_lex_pos(text, queries):
    """ Inefficient implementation of Task 1. Only for testing purposes. """
    result = []
    for query in queries:
        count = 0
        for string in text:
            if query < string:
                count += 1
        result.append(count)
    return result


def generate_prefixes(string):
    """ Generate all prefixes of a string """
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[0:i + 1])
    return prefixes


def random_string(threshold):
    """ Generate a random string of lowercase letters """
    letters = string.ascii_lowercase
    length = random.randint(0, threshold)
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str


class TestLexPos(unittest.TestCase):
    def test_provided(self):
        """ Provided in Assignment Spec """
        text = ["aaa", "bab", "aba", "baa", "baa", "aab", "bab"]
        queries = ["", "a", "b", "aab"]

        expected = [7, 7, 4, 5]
        actual = lex_pos(text, queries)
        self.assertEqual(expected, actual)

    def test_provided_extended(self):
        """ Assignment Spec Example but check for all possible prefixes """
        text = ["aaa", "bab", "aba", "baa", "baa", "aab", "bab"]
        queries = ["",
                   "a", "aa", "aaa",
                   "b", "ba", "bab",
                   "a", "ab", "aba",
                   "b", "ba", "baa",
                   "b", "ba", "baa",
                   "a", "aa", "aab",
                   "b", "ba", "bab"]

        expected = [7,
                    7, 7, 6,
                    4, 4, 0,
                    7, 5, 4,
                    4, 4, 2,
                    4, 4, 2,
                    7, 7, 5,
                    4, 4, 0]
        actual = lex_pos(text, queries)
        self.assertEqual(expected, actual)

    def test_empty_dataset(self):
        """ Text and Queries are empty """
        text = []
        queries = []

        expected = []
        actual = lex_pos(text, queries)
        self.assertEqual(expected, actual)

    def test_empty_string(self):
        """ Only empty string in text """
        text = ["", "", ""]
        queries = [""]

        expected = [0]
        actual = lex_pos(text, queries)
        self.assertEqual(expected, actual)

    def test_single_string(self):
        """ Only one string in text """
        text = ["hello"]
        queries = ["", "h", "he", "hel", "hell", "hello"]

        expected = [1, 1, 1, 1, 1, 0]
        actual = lex_pos(text, queries)
        self.assertEqual(expected, actual)

    def test_single_string_repeated(self):
        """ Only one string repeatedly inserted in text """
        text = ["world", "world", "world"]
        queries = ["", "w", "wo", "wor", "worl", "world"]

        expected = [3, 3, 3, 3, 3, 0]
        actual = lex_pos(text, queries)
        self.assertEqual(expected, actual)

    def test_prefixes_in_text(self):
        """ Check when there are items in text that are prefixes of other items in text """
        text = ["appleciders", "apple", "apple", "applecider", "appleciders", "app", "a", "", "app", ""]
        queries = ["", "a", "ap", "app", "appl", "apple", "applec", "appleci", "applecid", "applecide", "applecider", "appleciders"]

        expected = [8, 7, 7, 5, 5, 3, 3, 3, 3, 3, 2, 0]
        actual = lex_pos(text, queries)
        self.assertEqual(expected, actual)

    def test_different_branches(self):
        """ Check when every item in text is a unique branch in Trie """
        text = ["bravo", "alpha", "charlie", "echo", "omega", "november", "foxtrot", "alpha", "omega", "alpha"]
        queries = ["",
                   "b", "br", "bra", "brav", "bravo",
                   "a", "al", "alp", "alph", "alpha",
                   "c", "ch", "cha", "char", "charl", "charli", "charlie",
                   "e", "ec", "ech", "echo",
                   "o", "om", "ome", "omeg", "omega",
                   "n", "no", "nov", "nove", "novem", "novemb", "novembe", "november",
                   "f", "fo", "fox", "foxt", "foxtr", "foxtro", "foxtrot"]

        expected = [10,
                    7, 7, 7, 7, 6,
                    10, 10, 10, 10, 7,
                    6, 6, 6, 6, 6, 6, 5,
                    5, 5, 5, 4,
                    2, 2, 2, 2, 0,
                    3, 3, 3, 3, 3, 3, 3, 2,
                    4, 4, 4, 4, 4, 4, 3]
        actual = lex_pos(text, queries)
        self.assertEqual(expected, actual)

    def test_small_random(self):
        """ Small random case """
        text = [random_string(20) for _ in range(20)]
        queries = [""]
        for string in text:
            queries += generate_prefixes(string)

        expected = inefficient_lex_pos(text, queries)
        actual = lex_pos(text, queries)
        self.assertEqual(expected, actual)

    def test_medium_random(self):
        """ Medium random case """
        text = [random_string(100) for _ in range(200)]
        queries = [""]
        for string in text:
            queries += generate_prefixes(string)

        expected = inefficient_lex_pos(text, queries)
        actual = lex_pos(text, queries)
        self.assertEqual(expected, actual)

    def test_large_random(self):
        """ Large random case """
        text = [random_string(500) for _ in range(1000)]
        queries = [""]
        for string in text:
            queries += generate_prefixes(string)

        expected = inefficient_lex_pos(text, queries)
        actual = lex_pos(text, queries)
        self.assertEqual(expected, actual)

# %%
if __name__ == "__main__":
    unittest.main()

# %%
