"""
FIT2004 S2/2021 Assignment 3 Task 2 Test Cases

Split Arthur's test cases into smaller test cases,
granting more granular control, and more precise error msg.
(Yes, I failed so many cases I've to create my own :/ )

I pieced this thing together in a rush (bro I'm lazy).
This thing is unstable, and I might have omitted a few cases,
lemme know if anything is broken. I'll fix it if I've the time.

Contributions are welcomed.
Good luck with the assignment.

Credits:
Borrowed a few test cases from Arthur's & Michelle's.

Changelog:
  20210927 - Added empty-related cases
  20210928 - Added random test cases
  20210928 - Added one-is-longer / both equal size cases
"""

__author__ = 'Ci Leong Ong'


""" Imports """
import unittest
import random
from avl_tree import AVLTree


"""
Random test sizes

The following values dictate how many random tests
will be ran. Adjust the values as you like to avoid
lengthy tests.

For reference, running with the following parameters
took me 408.57s
"""
# Set this to False to switch off the random test cases
TEST_RANDOM = True

RANDOM_SMALL_TEST_SIZE = 5000 * int(TEST_RANDOM)
RANDOM_MEDIUM_TEST_SIZE = 500 * int(TEST_RANDOM)
RANDOM_LARGE_TEST_SIZE = 50 * int(TEST_RANDOM)


"""
Utility functions for checking invariants.

Opted out from efficiency for clear logic view.
"""

def is_balanced(avl) -> bool:
    """ Returns true if the AVL tree is balanced.

    Side effect:
    the height and balance of ALL nodes will be updated,
    if they used to be inaccurate, might cause confusion
    during the debugging process.

    TODO Write a side-effect free check
    """
    return avl.check_balanced()

def is_sorted(arr) -> bool:
    """ Returns true if array is sorted. """
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

def has_no_dupes(arr) -> bool:
    """ Returns true if array contains no duplicates. """
    return len(arr) == len(set(arr))

def are_mutually_exclusive(inlist, corrupted) -> bool:
    """
    Returns true if inlist and corrupted are mutually exclusive.
    TODO Optimise using binary search (inlist is sorted).
    """
    for key in corrupted:
        if key in inlist:
            return False
    return True

def is_subset(l1, l2) -> bool:
    """ Returns true if l1 is a subset of l2. """
    return set(l1).issubset(set(l2))

def no_missing_keys(t1_keys, t2_keys, corrupted, inlist) -> bool:
    """ Returns true if there are no missing keys in inlist. """
    return len(inlist) == len(t1_keys) - len(corrupted) + len(t2_keys)


class TestUncorruptedMerge(unittest.TestCase):

    def check_avl_invariant(self, t1_keys, t2_keys, corrupted, seed=None):
        """
        Helper method.
        Returns true if the AVL tree is valid.
        
        AVL invariant:
        i.   An AVL tree must be balanced.
        ii.  An AVL tree must satisfy BST's invariant.
               i.e. left_subtree < root < right_subtree
        iii. An AVL tree may not contain duplicate keys.

        Extra criteria for uncorrupted_merge:
        i.   The AVL tree may not contain corrupted keys.
        ii.  The AVL tree must contain as keys
             set(final_t2) in (set(t1) \ set(corrupted)) + set(t2)
             Not independent from case (i), so we will not
             check for corrupted keys:
             set(final_t2) in set(t1 + t2)
        iii. No keys are missing

        If there are any cases that I omitted, please
        add them here, the test cases will accommodate
        to the changes automatically.
        """
        # Check for runtime errors
        try:
            t1 = AVLTree(t1_keys)
            t2 = AVLTree(t2_keys)
            t2.uncorrupted_merge(t1, corrupted)
        except Exception as e:
            print(e, f'seed={seed}')
            # raise e

        # By the invariant of BST, inlist is a dupe-free
        # sorted list containing all keys in avl.
        inlist = t2.inorder_traverse()

        try:
            # AVL invariants
            self.assertTrue(is_balanced(t2), msg=f'Unbalanced tree, seed={seed}')
            self.assertTrue(is_sorted(inlist), msg=f'Not a BST - violated BST invariant, seed={seed}')
            self.assertTrue(has_no_dupes(inlist), msg=f'Contain dupe keys, seed={seed}')

            # uncorrupted_merge invariants
            self.assertTrue(are_mutually_exclusive(inlist, corrupted),
                msg=f'Merged tree contains corrupted key(s), seed={seed}')
            self.assertTrue(is_subset(inlist, t1_keys + t2_keys),
                msg=f'Merged tree contains keys that are not in original t1 or t2, seed={seed}')
            self.assertTrue(no_missing_keys(t1_keys, t2_keys, corrupted, inlist),
                msg=f'Some uncorrupted keys originally in t1 or t2 are missing, seed={seed}')
        except AssertionError as e:
            print()
            # Print tree to console for debugging
            t2.display()
            raise e

    def test_provided_example(self):
        """ Test case provided in the assignment specs."""
        t1_keys = [1, 2, 3, 4, 5]
        t2_keys = [6, 7, 8, 9, 10]
        corrupted = [1, 3, 5]
        self.check_avl_invariant(t1_keys, t2_keys, corrupted)

    """
    Edge cases: some of the inputs are empty.
    Don't bother testing more cases of these types,
    the cases tested here are exhaustive.

    x denotes empty input.

     t1     t2     corrupted
     x      x          x
                       x
            x
     x                 x        (t1 empty -> corrupted empty)
            x          x

    Cases are ALL borrowed from Arthur's test cases.
    """

    def test_empty_all(self):
        """ t1, t2, corrupted are empty.
        Creds: Arthur
        """
        t1_keys = []
        t2_keys = []
        corrupted = []
        self.check_avl_invariant(t1_keys, t2_keys, corrupted)

    def test_empty_corrupted(self):
        """ corrupted is empty.
        Creds: Arthur
        """
        t1_keys = [1, 2, 3, 4, 5]
        t2_keys = [6, 7, 8, 9, 10]
        corrupted = []
        self.check_avl_invariant(t1_keys, t2_keys, corrupted)

    def test_empty_t2(self):
        """ t2 is empty.
        Creds: Arthur
        """
        t1_keys = [1, 2, 3, 4, 5]
        t2_keys = []
        corrupted = [1, 3, 5]
        self.check_avl_invariant(t1_keys, t2_keys, corrupted)
    
    def test_empty_t1_corrupted(self):
        """ t1, corrupted are empty.
        Creds: Arthur
        """
        t1_keys = []
        t2_keys = [6, 7, 8, 9, 10]
        corrupted = []
        self.check_avl_invariant(t1_keys, t2_keys, corrupted)

    def test_empty_t2_corrupted(self):
        """ t2, corrupted are empty.
        Creds: Arthur
        """
        t1_keys = [1, 2, 3, 4, 5]
        t2_keys = []
        corrupted = []
        self.check_avl_invariant(t1_keys, t2_keys, corrupted)

    """
    Testing of the three independent cases:

    1. t1 > t2 (in size)
    2. t1 == t2
    3. t1 < t2
    """

    def test_self_longer(self):
        """
        More keys in self.
        Creds: Arthur
        """
        t1_keys = [4, -1, 0, 3, 6, 7, 9]
        t2_keys = [500, 454425, 32143, 234545435, 23434, 2313, 234, 23, 13, 45]
        corrupted = [0, -1]
        self.check_avl_invariant(t1_keys, t2_keys, corrupted)

    def test_self_longer(self):
        """ self and other are equal in size."""
        t1_keys = [4, -1, 0, 3, 6, 7, 9]
        t2_keys = [500, 454425, 32143, 234545435, 23434]
        corrupted = [0, -1]
        self.check_avl_invariant(t1_keys, t2_keys, corrupted)

    # def test_other_longer(self):
    #     """
    #     More keys in other.
    #     Creds: Arthur
    #     """
    #     t1_keys = [420, 0, -9, 3454, 421, 232, 12121, 9]
    #     t2_keys = [6969696969]
    #     corrupted = [420]
    #     self.check_avl_invariant(t1_keys, t2_keys, corrupted)

    """
    Random test cases

    Some cases are borrowed from Arthur's & Michelle's.
    TODO Swap for-loops to subtests, to avoid stopping the current
         test after a single exception is raised.
    """

    """ Small size cases """

    def test_completely_random_small(self):
        """ Completely random small cases."""
        for seed in range(0, RANDOM_SMALL_TEST_SIZE):
            # For reproducibility
            random.seed(seed)

            t1_keys = random.sample(range(-10000, 0), 20)
            t2_keys = random.sample(range(0, 10000), 20)
            corrupted = random.sample(t1_keys, random.randint(0, len(t1_keys)))
            self.check_avl_invariant(t1_keys, t2_keys, corrupted, seed)

    def test_random_small_t1_larger(self):
        """ Small random cases where # of keys of t1 > t2's."""
        for seed in range(0, RANDOM_SMALL_TEST_SIZE):
            # For reproducibility
            random.seed(seed)

            t1_keys = random.sample(range(-10000, 0), 25)
            t2_keys = random.sample(range(0, 10000), 20)
            # Ensure t1 is still larger after removing corrupted keys
            corrupted = random.sample(t1_keys, random.randint(0, len(t1_keys) - len(t2_keys)))
            self.check_avl_invariant(t1_keys, t2_keys, corrupted, seed)

    def test_random_small_t2_larger(self):
        """ Small random cases where # of keys of t2 > t1's."""
        for seed in range(0, RANDOM_SMALL_TEST_SIZE):
            # For reproducibility
            random.seed(seed)

            t1_keys = random.sample(range(-10000, 0), 24)
            t2_keys = random.sample(range(0, 10000), 25)
            corrupted = random.sample(t1_keys, random.randint(0, len(t1_keys)))
            self.check_avl_invariant(t1_keys, t2_keys, corrupted, seed)

    def test_random_small_t1_t2_equal_size(self):
        """ Small random cases where # of keys of t2 == t1's."""
        for seed in range(0, RANDOM_SMALL_TEST_SIZE):
            # For reproducibility
            random.seed(seed)

            t1_keys = random.sample(range(-10000, 0), 30)
            t2_keys = random.sample(range(0, 10000), 25)
            # Ensure t1 has same size as t2 after removing corrupted keys
            corrupted = random.sample(t1_keys, len(t1_keys) - len(t2_keys))
            self.check_avl_invariant(t1_keys, t2_keys, corrupted, seed)

    # """ Medium size cases """
    #
    # def test_completely_random_medium(self):
    #     """ Completely random medium cases."""
    #     for seed in range(0, RANDOM_MEDIUM_TEST_SIZE):
    #         # For reproducibility
    #         random.seed(seed)
    #
    #         t1_keys = random.sample(range(-10000, 0), 500)
    #         t2_keys = random.sample(range(0, 10000), 500)
    #         corrupted = random.sample(t1_keys, random.randint(0, len(t1_keys)))
    #         self.check_avl_invariant(t1_keys, t2_keys, corrupted, seed)
    #
    # def test_random_medium_t1_larger(self):
    #     """ Medium random cases where # of keys of t1 > t2's."""
    #     for seed in range(0, RANDOM_MEDIUM_TEST_SIZE):
    #         # For reproducibility
    #         random.seed(seed)
    #
    #         t1_keys = random.sample(range(-10000, 0), 750)
    #         t2_keys = random.sample(range(0, 10000), 500)
    #         # Ensure t1 is still larger after removing corrupted keys
    #         corrupted = random.sample(t1_keys, random.randint(0, len(t1_keys) - len(t2_keys)))
    #         self.check_avl_invariant(t1_keys, t2_keys, corrupted, seed)
    #
    # def test_random_medium_t2_larger(self):
    #     """ Medium random cases where # of keys of t2 > t1's."""
    #     for seed in range(0, RANDOM_MEDIUM_TEST_SIZE):
    #         # For reproducibility
    #         random.seed(seed)
    #
    #         t1_keys = random.sample(range(-10000, 0), 500)
    #         t2_keys = random.sample(range(0, 10000), 750)
    #         corrupted = random.sample(t1_keys, random.randint(0, len(t1_keys)))
    #         self.check_avl_invariant(t1_keys, t2_keys, corrupted, seed)
    #
    # def test_random_medium_t1_t2_equal_size(self):
    #     """ Medium random cases where # of keys of t2 == t1's."""
    #     for seed in range(0, RANDOM_MEDIUM_TEST_SIZE):
    #         # For reproducibility
    #         random.seed(seed)
    #
    #         t1_keys = random.sample(range(-10000, 0), 750)
    #         t2_keys = random.sample(range(0, 10000), 500)
    #         # Ensure t1 has same size as t2 after removing corrupted keys
    #         corrupted = random.sample(t1_keys, len(t1_keys) - len(t2_keys))
    #         self.check_avl_invariant(t1_keys, t2_keys, corrupted, seed)
    #
    # """ Large size cases """

    # def test_completely_random_large(self):
    #     """ Completely random large cases."""
    #     for seed in range(0, RANDOM_LARGE_TEST_SIZE):
    #         # For reproducibility
    #         random.seed(seed)
    #
    #         t1_keys = random.sample(range(-10000, 0), 7500)
    #         t2_keys = random.sample(range(0, 10000), 7500)
    #         corrupted = random.sample(t1_keys, random.randint(0, len(t1_keys)))
    #         self.check_avl_invariant(t1_keys, t2_keys, corrupted, seed)

    # def test_random_large_t1_larger(self):
    #     """ Large random cases where # of keys of t1 > t2's."""
    #     for seed in range(0, RANDOM_LARGE_TEST_SIZE):
    #         # For reproducibility
    #         random.seed(seed)
    #
    #         t1_keys = random.sample(range(-10000, 0), 10000)
    #         t2_keys = random.sample(range(0, 10000), 7500)
    #         # Ensure t1 is still larger after removing corrupted keys
    #         corrupted = random.sample(t1_keys, random.randint(0, len(t1_keys) - len(t2_keys)))
    #         self.check_avl_invariant(t1_keys, t2_keys, corrupted, seed)

    # def test_random_large_t2_larger(self):
    #     """ Large random cases where # of keys of t2 > t1's."""
    #     for seed in range(0, RANDOM_LARGE_TEST_SIZE):
    #         # For reproducibility
    #         random.seed(seed)
    #
    #         t1_keys = random.sample(range(-10000, 0), 7500)
    #         t2_keys = random.sample(range(0, 10000), 10000)
    #         corrupted = random.sample(t1_keys, random.randint(0, len(t1_keys)))
    #         self.check_avl_invariant(t1_keys, t2_keys, corrupted, seed)

    # def test_random_large_t1_t2_equal_size(self):
    #     """ Large random cases where # of keys of t2 == t1's."""
    #     for seed in range(0, RANDOM_LARGE_TEST_SIZE):
    #         # For reproducibility
    #         random.seed(seed)
    #
    #         t1_keys = random.sample(range(-10000, 0), 10000)
    #         t2_keys = random.sample(range(0, 10000), 7500)
    #         # Ensure t1 has same size as t2 after removing corrupted keys
    #         corrupted = random.sample(t1_keys, len(t1_keys) - len(t2_keys))
    #         self.check_avl_invariant(t1_keys, t2_keys, corrupted, seed)


if __name__ == '__main__':
    unittest.main()
