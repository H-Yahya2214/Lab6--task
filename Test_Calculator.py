import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = Calculator.add(4, 9)
        self.assertEqual(result, 13)

        result = Calculator.add(1, 3)
        self.assertEqual(result, 4)

        result = Calculator.add(20, 5)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()
