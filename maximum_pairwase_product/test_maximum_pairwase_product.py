#!/usr/bin/env python3

import unittest
from maximum_pairwise_product import *

class MaximumPairwiseProductTestCase(unittest.TestCase):

    def test_unexpected_input(self):
        numbers = ''
        with self.assertRaises(TypeError):
            maximum_pairwise_product(numbers)
        
    def test_empty(self):
        numbers = []
        with self.assertRaises(IndexError):
            maximum_pairwise_product(numbers)

    def test_one_number(self):
        numbers = [3]
        with self.assertRaises(IndexError):
            maximum_pairwise_product(numbers)

    def test_multiple_numbers(self):
        numbers = [1, 5, 4, 6, 8]
        result = maximum_pairwise_product(numbers)
        self.assertEqual(48, result)

    def test_invalid_items(self):
        numbers = [1, 6, 7, 5, 'u', 8]
        with self.assertRaises(ValueError):
            maximum_pairwise_product(numbers)    
                        

if __name__ == "__main__":
    unittest.main()
