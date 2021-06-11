#!/usr/bin/env python3

import unittest
from last_digit_sum_fibonacci import *

class LastDigitFibTestCase(unittest.TestCase):

    def test_0(self):
        result = last_digit_fib(0)
        self.assertEqual(0, result)

    def test_2(self):
        result = last_digit_fib(2)
        self.assertEqual(1, result)

    def test_8(self):
        result = last_digit_fib(8)
        self.assertEqual(1, result)

    def test_big_num(self):
        result = last_digit_fib(1000000)
        self.assertEqual(5, result)

class CalculateLastDigitSumTestCase(unittest.TestCase):

    def test_small_n(self):
        n = 3
        result = calculate_last_digit_sum(n)
        self.assertEqual(4, result)

    def test_bigger_n(self):
        n = 100
        result = calculate_last_digit_sum(n)
        self.assertEqual(5, result)


if __name__ == "__main__":
    unittest.main()
