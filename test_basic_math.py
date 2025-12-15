import unittest
from basic_math import addition, soustration, multiplication, division, modulo, exponentiation, binary

class TestBasicMath(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(200, 100), 300)

    def test_soustration(self):
        self.assertEqual(soustration(5, 3), 2)
        self.assertEqual(soustration(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 5), 20)
        self.assertEqual(multiplication(-1, 1), -1)

    def test_division(self):
        self.assertEqual(division(10, 2),5)
        self.assertEqual(division(10, 0),)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(10, 2), 0)

    def test_exponentiation(self):
        self.assertEqual(exponentiation(2, 3), 8)
        self.assertEqual(exponentiation(5, 0), 1)

    def test_binary(self):
        self.assertEqual(binary(10), '1010')
        self.assertEqual(binary(0), '')

if __name__ == '__main__':
    unittest.main()