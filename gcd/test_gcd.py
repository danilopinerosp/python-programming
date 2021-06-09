#!/usr/bin/env python3

import unittest
from gcd import *

class EuclideanGCDTestCase(unittest.TestCase):

    def test_small_numbers(self):
        result = euclidean_gcd(5, 2)
        self.assertEqual(1, result)

    def test_different_big_numbers(self):
        result = euclidean_gcd(578678, 65747)
        self.assertEqual(1, result)

    def test_same_number(self):
        result = euclidean_gcd(465, 465)
        self.assertEqual(465, result)

    def test_second_bigger(self):
        result = euclidean_gcd(4, 12)
        self.assertEqual(4, result)


if __name__ == "__main__":
    unittest.main()
