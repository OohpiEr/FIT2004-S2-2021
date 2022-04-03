""" Unit tests for Task 2 of FIT2004 Assignment 3 """

__author__ = "Arthur Lee"

import unittest
import random
from avl_tree import AVLTree


def produce_avl_trees(t1_keys, t2_keys):
    """ Helper Function to create two AVL trees from two lists of keys """
    t1 = AVLTree()
    for item in t1_keys:
        t1.insert(item)
    t2 = AVLTree()
    for item in t2_keys:
        t2.insert(item)
    return t1, t2


class TestUncorruptedMerge(unittest.TestCase):
    def test_provided(self):
        """ Provided in Assignment Spec """
        t1 = [1, 2, 3, 4, 5]
        t2 = [6, 7, 8, 9, 10]
        t1, t2 = produce_avl_trees(t1, t2)
        corrupted = [1, 3, 5]

        expected = sorted([2, 4, 6, 7, 8, 9, 10])
        t2.uncorrupted_merge(t1, corrupted)
        actual = t2.inorder_traverse()

        self.assertEqual(expected, actual, msg="Keys in self are not correct or break the AVL Tree invariant")
        try:
            self.assertTrue(t2.check_balanced(), msg="self is not balanced")
        except AssertionError as e:
            print()
            t2.display()
            raise e

    def test_empty_everything(self):
        """ self, other, corrupted are empty """
        myself = []
        other = []
        myself, other = produce_avl_trees(myself, other)
        corrupted = []

        expected = sorted([])
        myself.uncorrupted_merge(other, corrupted)
        actual = myself.inorder_traverse()

        self.assertEqual(expected, actual, msg="Keys in self are not correct or break the AVL Tree invariant")
        try:
            self.assertTrue(myself.check_balanced(), msg="self is not balanced")
        except AssertionError as e:
            print()
            myself.display()
            raise e

    def test_empty_corrupted(self):
        """ Only corrupted is empty """
        myself = [5, 1, 4, 9, 0, -1, 3]
        other = [-9, -2, -4, -6, -100]
        myself, other = produce_avl_trees(myself, other)
        corrupted = []

        expected = sorted([5, 1, 4, 9, 0, -1, 3, -9, -2, -4, -6, -100])
        myself.uncorrupted_merge(other, corrupted)
        actual = myself.inorder_traverse()

        self.assertEqual(expected, actual, msg="Keys in self are not correct or break the AVL Tree invariant")
        try:
            self.assertTrue(myself.check_balanced(), msg="self is not balanced")
        except AssertionError as e:
            print()
            myself.display()
            raise e

    def test_empty_other_corrupted(self):
        """ other and corrupted are empty """
        myself = [9.9, 10, 100.3242, 98.9, 45, 98, 69]
        other = []
        myself, other = produce_avl_trees(myself, other)
        corrupted = []

        expected = sorted([9.9, 10, 100.3242, 98.9, 45, 98, 69])
        myself.uncorrupted_merge(other, corrupted)
        actual = myself.inorder_traverse()

        self.assertEqual(expected, actual, msg="Keys in self are not correct or break the AVL Tree invariant")
        try:
            self.assertTrue(myself.check_balanced(), msg="self is not balanced")
        except AssertionError as e:
            print()
            myself.display()
            raise e

    def test_empty_self(self):
        """ self is empty """
        myself = []
        other = [69, -0.4, 223, 324234, 13, 420]
        myself, other = produce_avl_trees(myself, other)
        corrupted = [420, 69]

        expected = sorted([-0.4, 223, 324234, 13])
        myself.uncorrupted_merge(other, corrupted)
        actual = myself.inorder_traverse()

        self.assertEqual(expected, actual, msg="Keys in self are not correct or break the AVL Tree invariant")
        try:
            self.assertTrue(myself.check_balanced(), msg="self is not balanced")
        except AssertionError as e:
            print()
            myself.display()
            raise e

    def test_empty_self_corrupted(self):
        """ self and corrupted are empty """
        myself = []
        other = [450, 89, 0.999999, 234, -1, 3249]
        myself, other = produce_avl_trees(myself, other)
        corrupted = []

        expected = sorted([450, 89, 0.999999, 234, -1, 3249])
        myself.uncorrupted_merge(other, corrupted)
        actual = myself.inorder_traverse()

        self.assertEqual(expected, actual, msg="Keys in self are not correct or break the AVL Tree invariant")
        try:
            self.assertTrue(myself.check_balanced(), msg="self is not balanced")
        except AssertionError as e:
            print()
            myself.display()
            raise e

    def test_self_longer(self):
        """ More keys in self """
        myself = [500, 454425, 32143, 234545435, 23434, 2313, 234, 23, 13, 45]
        other = [4, -1, 0, 3, 6, 7, 9]
        myself, other = produce_avl_trees(myself, other)
        corrupted = [0, -1]

        expected = sorted([500, 454425, 32143, 234545435, 23434, 2313, 234, 23, 13, 45, 4, 3, 6, 7, 9])
        myself.uncorrupted_merge(other, corrupted)
        actual = myself.inorder_traverse()

        self.assertEqual(expected, actual, msg="Keys in self are not correct or break the AVL Tree invariant")
        try:
            self.assertTrue(myself.check_balanced(), msg="self is not balanced")
        except AssertionError as e:
            print()
            myself.display()
            raise e

    # def test_other_longer(self):
    #     """ More keys in other """
    #     myself = [6969696969]
    #     other = [420, 0, -9, 3454, 421, 232, 12121, 9]
    #     myself, other = produce_avl_trees(myself, other)
    #     corrupted = [420]
    #     print("----- self ------")
    #     myself.display()
    #     print("----- other ------")
    #     other.display()
    #
    #     expected = sorted([6969696969, 0, -9, 3454, 421, 232, 12121, 9])
    #     myself.uncorrupted_merge(other, corrupted)
    #     actual = myself.inorder_traverse()
    #
    #     self.assertEqual(expected, actual, msg="Keys in self are not correct or break the AVL Tree invariant")
    #     try:
    #         self.assertTrue(myself.check_balanced(), msg="self is not balanced")
    #     except AssertionError as e:
    #         print()
    #
    #         print("----- actual ------")
    #         myself.display()
    #         print("----- expected ------")
    #         expected_tree = AVLTree()
    #         for item in expected:
    #             expected_tree.insert(item)
    #         expected_tree.display()
    #         raise e

    def test_small_random(self):
        """ Small Random Test """
        myself_items = random.sample(range(0, 10000), 21)
        other_items = random.sample(range(-10000, -1), 20)
        myself, other = produce_avl_trees(myself_items, other_items)

        corrupted = []
        indexes = random.sample(range(0, 19), 4)
        for index in indexes:
            corrupted.append(other_items[index])

        for key in corrupted:
            other_items.remove(key)
        expected = sorted(myself_items + other_items)
        myself.uncorrupted_merge(other, corrupted)
        actual = myself.inorder_traverse()

        self.assertEqual(expected, actual, msg="Keys in self are not correct or break the AVL Tree invariant")
        try:
            self.assertTrue(myself.check_balanced(), msg="self is not balanced")
        except AssertionError as e:
            print()
            myself.display()
            raise e

    def test_medium_random(self):
        """ Medium Random Test """
        myself_items = random.sample(range(400, 10000), 500)
        other_items = random.sample(range(-10000, 399), 501)
        myself, other = produce_avl_trees(myself_items, other_items)

        corrupted = []
        indexes = random.sample(range(0, 500), 42)
        for index in indexes:
            corrupted.append(other_items[index])

        for key in corrupted:
            other_items.remove(key)
        expected = sorted(myself_items + other_items)
        myself.uncorrupted_merge(other, corrupted)
        actual = myself.inorder_traverse()

        self.assertEqual(expected, actual, msg="Keys in self are not correct or break the AVL Tree invariant")
        try:
            self.assertTrue(myself.check_balanced(), msg="self is not balanced")
        except AssertionError as e:
            print()
            myself.display()
            raise e

    def test_large_random(self):
        """ Large Random Test """
        myself_items = random.sample(range(0, 10005), 5000)
        other_items = random.sample(range(-10005, -1), 5000)
        myself, other = produce_avl_trees(myself_items, other_items)

        corrupted = []
        indexes = random.sample(range(0, 4999), 167)
        for index in indexes:
            corrupted.append(other_items[index])

        for key in corrupted:
            other_items.remove(key)
        expected = sorted(myself_items + other_items)
        myself.uncorrupted_merge(other, corrupted)
        actual = myself.inorder_traverse()

        self.assertEqual(expected, actual, msg="Keys in self are not correct or break the AVL Tree invariant")
        try:
            self.assertTrue(myself.check_balanced(), msg="self is not balanced")
        except AssertionError as e:
            print()
            myself.display()
            raise e


if __name__ == "__main__":
    unittest.main()
