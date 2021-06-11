#!/usr/bin/env python3


import unittest
from fibonacci_module import *

class PisanoPeriodTestCase(unittest.TestCase):

    def test_1(self):
        period = pisano_period(1)
        self.assertEqual(1, period)

    def test_2(self):
        period = pisano_period(2)
        self.assertEqual(3, period)

    def test_3(self):
        period = pisano_period(3)
        self.assertEqual(8, period)

    def test_6(self):
        period = pisano_period(6)
        self.assertEqual(24, period)

    def test_98(self):
        period = pisano_period(98)
        self.assertEqual(336, period)


class FibonacciModuleTestCase(unittest.TestCase):

    def test_small_n(self):
        n = 239
        m = 1000
        result = fibonacci_module(n, m)
        self.assertEqual(161, result)

    def test_big_n(self):
        n = 2816213588
        m = 239
        result = fibonacci_module(n, m)
        self.assertEqual(151, result)

if __name__ == "__main__":
    unittest.main()
