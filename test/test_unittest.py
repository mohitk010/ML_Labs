import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(5, 0), 5)
        
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.substract(2, 3), -1)
        self.assertEqual(calculator.substract(5, 0), 5)
        self.assertEqual(calculator.substract(-1, 1), -2)
        self.assertEqual(calculator.substract(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(5, 0), 0)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.add_3_nums(2, 3, 5), 10)
        self.assertEqual(calculator.add_3_nums(5, 0, -1), 4)
        self.assertEqual(calculator.add_3_nums(-1, -1, -1), -3)
        self.assertEqual(calculator.add_3_nums(-1, -1, 100), 98)



if __name__ == '__main__':
    unittest.main()