#!/usr/bin/env python3

import unittest
from coc_resto import coc_resto

class TestCocResto(unittest.TestCase):

    def test_sin_resto(self):
        expected = (4, 0)
        self.assertEqual(coc_resto(8, 2), expected)

    def test_con_resto(self):
        expected = (5, 1)
        self.assertEqual(coc_resto(16, 3), expected)

unittest.main()
