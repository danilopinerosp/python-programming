#!/usr/bin/env python3

import unittest
from lcm import *

class CalculateLCMTestCase(unittest.TestCase):

    def test_both_1(self):
        result = calculate_lcm(1, 1)
        self.assertEqual(1, result)

    def test_small_different(self):
        result = calculate_lcm(6, 8)
        self.assertEqual(24, result)

    def test_big_and_small_numbers(self):
        result = calculate_lcm(2, 9569873)
        self.assertEqual(19139746, result)

unittest.main()
