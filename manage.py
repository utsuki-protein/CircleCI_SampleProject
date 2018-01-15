# -*- coding:utf-8 -*-
import unittest
import calc


class TestClass(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calc.addition(2, 3), 4)
        self.assertEqual(calc.addition(0, 0), 0)
        self.assertEqual(calc.addition(7, 3), 10)

    def test_subtraction(self):
        self.assertEqual(calc.subtraction(3, 1), 2)
        self.assertEqual(calc.subtraction(3, 4), -1)
        self.assertEqual(calc.subtraction(1, 0), 1)

    def test_multiplication(self):
        self.assertEqual(calc.multiplication(1, 2), 2)
        self.assertEqual(calc.multiplication(3, 5), 15)
        self.assertEqual(calc.multiplication(4, 0), 0)

    def test_division(self):
        self.assertEqual(calc.division(6, 2), 3)
        self.assertEqual(calc.division(5, 2), 2.5)
        self.assertEqual(calc.division(5, 0), 0)

if __name__ == '__main__':
    unittest.main()
