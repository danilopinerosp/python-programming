#!/usr/bin/env python3

import unittest
from factores_primos import factores_primos, es_primo

class EsPrimoTestCase(unittest.TestCase):

    def test_es_primo_negativo(self):
        self.assertFalse(es_primo(-5))

    def test_es_primo_0(self):
        self.assertFalse(es_primo(0))

    def test_es_primo_1(self):
        self.assertFalse(es_primo(1))

    def test_es_primo_2(self):
        self.assertTrue(es_primo(2))

    def test_es_primo_3(self):
        self.assertTrue(es_primo(3))

    def test_es_primo_4(self):
        self.assertFalse(es_primo(4))

    def test_es_primo_17(self):
        self.assertTrue(es_primo(17))

class FactoresPrimosTestCase(unittest.TestCase):

    def test_factores_primos_0(self):
        resultado = factores_primos(0)
        self.assertEqual([], resultado)

    def test_factores_primos_1(self):
        resultado = factores_primos(1)
        self.assertEqual([], resultado)

    def test_factores_primos_2(self):
        resultado = factores_primos(2)
        self.assertEqual([2], resultado)

    def test_factores_primos_6(self):
        resultado = factores_primos(6)
        self.assertEqual([2, 3], resultado)

    def test_factores_primos_11(self):
        resultado = factores_primos(11)
        self.assertEqual([11], resultado)

    def test_factores_primos_18(self):
        resultado = factores_primos(18)
        self.assertEqual([2, 3, 3], resultado)

if __name__ == "__main__":
    unittest.main()
        

    
