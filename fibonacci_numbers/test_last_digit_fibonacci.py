#!/usr/bin/env python3

import unittest
from last_digit_fibonacci import *

class LastDigitFibonacciTestCase(unittest.TestCase):

    def test_basecase_0(self):
        digit = last_digit_fibonacci(0)
        self.assertEqual(0, digit)
        
    def test_number_one_digit(self):
        digit = last_digit_fibonacci(5)
        self.assertEqual(5, digit)

    def test_number_two_digits(self):
        digit = last_digit_fibonacci(8) # fib number of 8 is 21
        self.assertEqual(1, digit)

    def test_huge_case_327305(self):
        digit = last_digit_fibonacci(327305)
        self.assertEqual(5, digit)

if __name__ == "__main__":
    unittest.main()
