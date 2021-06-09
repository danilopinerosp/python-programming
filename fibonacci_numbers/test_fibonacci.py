#!/usr/bin/env python3

import unittest
from fibonacci import *

class FibRecursTestCase(unittest.TestCase):

    def test_basecase_0(self):
        result = fib_recurs(0)
        self.assertEqual(0, result)

    def test_basecase_1(self):
        result = fib_recurs(1)
        self.assertEqual(1, result)

    def test_2(self):
        result = fib_recurs(2)
        self.assertEqual(1, result)

    def test_5(self):
        result = fib_recurs(5)
        self.assertEqual(5, result)

    @unittest.skip('The recursive algorithm is too slow')
    def test_big_number_500(self):
        result = fib_recurs(500)
        fib_n = 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
        self.assertEqual(fib_n, result)



class FibListTestCase(unittest.TestCase):

    def test__0(self):
        result = fib_list(0)
        self.assertEqual(0, result)

    def test_1(self):
        result = fib_list(1)
        self.assertEqual(1, result)

    def test_8(self):
        result = fib_list(8)
        self.assertEqual(21, result)

    def test_big_number_500(self):
        result = fib_list(500)
        fib_n = 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
        self.assertEqual(fib_n, result)


if __name__ == "__main__":
    unittest.main()
