"""
Test cases for FIT2004 2021 S2 Assignment 2 Task 2.
"""

import unittest
from assignment2 import best_lamp_allocation


class TestBestLampAllocation(unittest.TestCase):

    def test1(self):
        """ Provided example in assignment specs."""
        probs = [
            [ 0.5 , 0.5 , 1    ] , 
            [ 0.25, 0.1 , 0.75 ]
        ]
        result = best_lamp_allocation(len(probs), 2, probs)
        expected_result = 0.375
        self.assertEqual(result, expected_result, msg=f'Cannot allocate all lamps for best outcome. Expected {expected_result}, got {result}.')

        probs = [
            [ 0.5 , 0.75, 0.25 ] ,
            [ 0.75, 0.25, 0.8  ]
        ]
        result = best_lamp_allocation(len(probs), 2, probs)
        expected_result = 0.5625
        self.assertEqual(result, expected_result, msg=f'Cannot allocate required lamps for best outcome. Expected {expected_result}, got {result}.')

    def test2(self):
        """ Edge case: Largest element in list is 0.
        """
        probs = [
            [0] ,
            [0]
        ]
        result = best_lamp_allocation(len(probs), 2, probs)
        expected_result = 0
        self.assertEqual(result, expected_result, msg=f'Cannot allocate lamps when all 0. Expected {expected_result}, got {result}.')
    
    def test3(self):
        """ Different dimension matrix L*P, L!=P.
        """
        probs = [
            [ 0.5 , 0.75, 0.25 ] ,
            [ 0.75, 0.25, 0.8  ] ,
            [ 0.4 , 0.3 , 0.5  ]
        ]
        result = best_lamp_allocation(len(probs), 2, probs)
        expected_result = 0.225
        self.assertEqual(result, expected_result, msg=f'Cannot allocate for different dimension matrix. Expected {expected_result}, got {result}.')
    
    def test4(self):
        """ Lamps available is more than plants 
        """
        probs = [
            [0.2, 0.5, 1], 
            [0.3, 0.7, 0.6], 
        ]
        result = best_lamp_allocation(len(probs), 3, probs)
        expected_result = 0.7
        self.assertEqual(result, expected_result, msg=f'Cannot allocate when there are more lamps than plants. Expected {expected_result}, got {result}.')

    def test5(self):
        """ Lots of lamps available 
        """
        probs = [
            [0.2, 0.5, 1, 0.4], 
            [0.3, 0.7, 0.9, 0.7], 
        ]
        result = best_lamp_allocation(len(probs), 999, probs)
        expected_result = 0.9
        self.assertEqual(result, expected_result, msg=f'Cannot allocate best when lost of lamps available. Expected {expected_result}, got {result}.')

if __name__ == '__main__':
    unittest.main()