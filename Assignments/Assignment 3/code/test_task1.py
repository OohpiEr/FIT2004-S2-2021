"""Test Cases for Question 1 of FIT2004 Assignment 2"""

__author__ = "Chee Min Hao"

import unittest
from string import ascii_lowercase
import random
from task1 import lex_pos
from time import time

# %%
class TestLexPos(unittest.TestCase):
    def test1(self):
        """
        Test Case Sample from Assignment
        (includes duplicate elements and empty queries)
        """
        text = ["aaa","bab","aba","baa","baa","aab","bab"]
        queries = ["", "a", "b", "aab"]
        expected = [7, 7, 4, 5]
        result = lex_pos(text, queries)
        self.assertEqual(result, expected, msg=f'Expected {expected} but got {result}')

    def test2(self):
        """
        Queries which are 1 < n < len(max(queries))
        """
        text = ["lmao", "heya", "cowabunga", "crazy", "bruh"]
        queries = ["lma", "hey", "cowab"]
        expected = [1, 2, 4]
        result = lex_pos(text, queries)
        self.assertEqual(result, expected, msg=f'Expected {expected} but got {result}')

    def test3(self):
        """
        Very random string example
        """
        # text = [(''.join(random.choice(ascii_lowercase) for _ in range(10))) for _ in range(50)]
        # queries = [(''.join(random.choice(ascii_lowercase) for _ in range(5))) for _ in range(5)]
        text = ['vywpqkwdhb', 'bdtphukeoo', 'zoikqudcda', 'ebrimooyls', 'vnreucivdq', 'mnjlhbhpxv', 'tefiqxffae', 'gbahwdfjnb', 'kpwdunejfm', 'qbexmmdxns']
        queries = ['vywp', 'z', 'ebrimooy', 'mn']
        expected = [2, 1, 9, 6]
        result = lex_pos(text, queries)
        self.assertEqual(result, expected, msg=f'Expected {expected} but got {result}')

    def test4(self):
        """
        Queries contain elements which are exactly same as one of the elements in text
        but that element is not of the longest length in text
        """
        text = ["aab","a","ab","aac","aab"]
        queries = ["ab", "a"]
        expected = [0, 4]
        result = lex_pos(text, queries)
        self.assertEqual(result, expected, msg=f'Expected {expected} but got {result}')

    def test5(self):
        """
        text and queries are both empty
        """
        text = []
        queries = []
        expected = []
        result = lex_pos(text, queries)
        self.assertEqual(result, expected, msg=f'Expected {expected} but got {result}')

    def test6(self):
        """
        text is non empty but queries is empty
        """
        text = ["aas", "aba", "cab"]
        queries = []
        expected = []
        result = lex_pos(text, queries)
        self.assertEqual(result, expected, msg=f'Expected {expected} but got {result}')

    def test7(self):
        """
        queries has repeated strings
        """
        text = ["aab","a","ab","aac","aab"]
        queries = ["aa", "aa", "aa"]
        expected = [4, 4, 4]
        result = lex_pos(text, queries)
        self.assertEqual(result, expected, msg=f'Expected {expected} but got {result}')


    # def test3(self):
    #     text = [(''.join(random.choice(ascii_lowercase) for _ in range(10))) for _ in range(10000000)]
    #     queries = [(''.join(random.choice(ascii_lowercase) for _ in range(7))) for _ in range(100000)]
    #     start = time()
    #     lex_pos(text, queries)
    #     end = time()
    #     print()
    #     print(f'Time Taken = {start - end}')

# %%
if __name__ == "__main__":
    unittest.main()

        
# %%
