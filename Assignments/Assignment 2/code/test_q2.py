""" Test cases for Question 2 of FIT2004 Assignment 2 """

__author__ = "Arthur Lee"

import unittest
import random
from assignment2 import best_lamp_allocation


class TestBestLampAllocation(unittest.TestCase):
    def test1(self):
        """ Provided Example in Assignment Spec """
        probs = [[0.5,  0.5, 1],
                 [0.25, 0.1, 0.75]]
        actual = best_lamp_allocation(2, 2, probs)
        expected = 0.375
        self.assertAlmostEqual(expected, actual)

    def test2(self):
        """ Provided Example in Assignment Spec """
        probs = [[0.5,  0.75, 0.25],
                 [0.75, 0.25, 0.8]]
        actual = best_lamp_allocation(2, 2, probs)
        expected = 0.5625
        self.assertAlmostEqual(expected, actual)

    def test3(self):
        """ Extra Example Provided """
        probs = [[0.92, 0.88, 0.07, 0.74, 0.83, 0.73, 0.85, 0.41, 0.94, 0.58, 0.17],
                 [0.05, 0.42, 0.01, 0.53, 0.03, 0.13, 0.49, 0.64, 0.13, 0.78, 0.05],
                 [0.68, 0.38, 0.86, 0.6, 0.53, 0.49, 0.89, 0.18, 0.69, 0.21, 0.3],
                 [0.61, 0.85, 0.17, 0.78, 0.21, 0.05, 0.09, 0.7, 0.08, 0.86, 0.21],
                 [0.72, 0.81, 0.12, 0.73, 0.45, 0.8, 0.3, 0.84, 0.89, 0.48, 0.33],
                 [0.19, 0.33, 0.01, 0.54, 0.71, 0.56, 0.55, 0.28, 0.29, 0.43, 0.42],
                 [0.36, 0.65, 0.38, 0.48, 0.05, 0.28, 0.45, 0.42, 0.49, 0.5, 0.97],
                 [0.95, 0.05, 0.73, 0.91, 0.25, 0.16, 0.11, 0.67, 0.48, 0.48, 0.77],
                 [0.96, 0.21, 0.19, 0.55, 0.04, 0.58, 0.91, 0.3, 0.92, 0.36, 0.48],
                 [0.46, 0.6, 0.76, 0.91, 0.79, 0.92, 0.66, 0.28, 0.48, 0.32, 0.17]]
        actual = best_lamp_allocation(10, 10, probs)
        expected = 0.061589317090129915
        self.assertAlmostEqual(expected, actual)

    def test4(self):
        """ Extra Example Provided """
        probs = [[0.39, 0.53, 0.09, 0.13, 0.36, 0.91, 0.84, 0.14, 0.3, 0.23, 0.21],
                 [0.31, 0.49, 0.99, 0.13, 0.45, 0.7, 0.73, 0.22, 0.97, 0.89, 0.93],
                 [0.08, 0.73, 0.17, 0.24, 0.62, 0.69, 0.43, 0.31, 0.79, 0.73, 0.96],
                 [0.42, 0.1, 0.97, 0.27, 0.5, 0.84, 0.32, 0.53, 0.31, 0.22, 0.93],
                 [0.45, 0.51, 0.99, 0.86, 0.22, 0.62, 0.45, 0.47, 0.83, 0.88, 0.85],
                 [0.68, 0.35, 0.5, 0.06, 0.14, 0.88, 0.51, 0.84, 0.35, 0.12, 0.38],
                 [0.86, 0.64, 0.78, 0.17, 0.24, 0.69, 0.4, 0.72, 0.74, 0.14, 0.97],
                 [0.48, 0.02, 0.48, 0.09, 0.73, 0.37, 0.68, 0.34, 0.49, 0.28, 0.37],
                 [0.69, 0.25, 0.46, 0.2, 0.68, 0.73, 0.83, 0.26, 0.92, 0.74, 0.97],
                 [1.0, 0.57, 0.77, 0.55, 0.79, 0.54, 0.07, 0.89, 0.38, 0.55, 0.87]]
        actual = best_lamp_allocation(10, 10, probs)
        expected = 0.07124240062011918
        self.assertAlmostEqual(expected, actual)

    def test5(self):
        """ Empty probs list and No Resources """
        probs = []
        actual = best_lamp_allocation(0, 0, probs)
        expected = 1
        self.assertAlmostEqual(expected, actual)

    def test6(self):
        """ One Plant, No Lamps """
        probs = [[0.9]]
        actual = best_lamp_allocation(1, 0, probs)
        expected = 0.9
        self.assertAlmostEqual(expected, actual)

    def test7(self):
        """ Multiple Plants, No Lamps """
        probs = [[0.9],
                 [0],
                 [1]]
        actual = best_lamp_allocation(3, 0, probs)
        expected = 0
        self.assertAlmostEqual(expected, actual)

    def test8(self):
        """ One plant Multiple Lamps """
        probs = [[0.1, 0.3, 0.2]]
        num_l = 2
        num_p = 1
        expected = 0.3
        actual = best_lamp_allocation(num_p, num_l, probs)
        self.assertAlmostEqual(expected, actual)

    def test9(self):
        """ Small Random Case """
        P = 10
        L = 10
        probs = [None] * P
        for i in range(P):
            probs[i] = [None] * (L + 1)
        for i in range(P):
            for j in range(L + 1):
                random.seed(i + j)
                probs[i][j] = random.random()
        result = best_lamp_allocation(P, L, probs)
        print()
        print("Q2 Small Random Case: " + str(result))

    def test10(self):
        """ Medium Random Case """
        P = 50
        L = 50
        probs = [None] * P
        for i in range(P):
            probs[i] = [None] * (L + 1)
        for i in range(P):
            for j in range(L + 1):
                random.seed(i - j)
                probs[i][j] = random.random()
        result = best_lamp_allocation(P, L, probs)
        print()
        print("Q2 Medium Random Case: " + str(result))

    # def test11(self):
    #     """ Large Random Case """
    #     P = 1000
    #     L = 1000
    #     probs = [None] * P
    #     for i in range(P):
    #         probs[i] = [None] * (L + 1)
    #     for i in range(P):
    #         for j in range(L + 1):
    #             random.seed(i * j)
    #             probs[i][j] = random.random()
    #     result = best_lamp_allocation(P, L, probs)
    #     print()
    #     print("Q2 Large Random Case: " + str(result))

    def test12(self):
        """ Empty probs list but tons of Resources """
        probs = []
        actual = best_lamp_allocation(234, 269, probs)
        expected = 0
        self.assertAlmostEqual(expected, actual)
    

    def test13(self):
        """ Less Lamps than in probs """
        probs = [[0.4, 0.75, 0.9],
                 [0.8, 0.25, 0.4]]
        actual = best_lamp_allocation(2, 1, probs)
        expected = 0.6
        self.assertAlmostEqual(expected, actual)
    
    def test14(self):
        """ Less Plants than in probs """
        probs = [[0.4, 0.75, 0.9],
                 [0.8, 0.25, 0.4],
                 [0.9, 0.1, 0.6]]
        actual = best_lamp_allocation(2, 2, probs)
        expected = 0.72
        self.assertAlmostEqual(expected, actual)
    
    def test15(self):
        """ More Lamps than in probs """
        probs = [[0, 0.75, 1],
                 [0.3, 0.1, 0.95]]
        actual = best_lamp_allocation(2, 234, probs)
        expected = 0.95
        self.assertAlmostEqual(expected, actual)
    
    def test16(self):
        """ More Plants than in probs """
        probs = [[0, 0.75, 1],
                 [0.3, 0.1, 0.95]]
        actual = best_lamp_allocation(200, 2, probs)
        expected = 0
        self.assertAlmostEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
