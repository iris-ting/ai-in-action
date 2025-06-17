# test_subtract.py
import unittest
from subtract import subtract

class TestSubtract(unittest.TestCase):
    """
    Test strategy:
    We will test the subtract function with the following test cases:
    1.  Positive numbers: Check if the function correctly subtracts positive numbers.
    2.  Negative numbers: Check if the function correctly subtracts negative numbers.
    3.  Zero: Check if the function correctly handles zero as an input.
    4.  Mixed positive and negative numbers: Check if the function correctly subtracts a positive number from a negative number and vice versa.

    We will use the assertEqual method to check if the actual output of the function matches the expected output.
    """

    def test_positive_numbers(self):
        self.assertEqual(subtract(5, 2), 2, "Should return 2")

    def test_negative_numbers(self):
        self.assertEqual(subtract(-5, -2), -4, "Should return -4")

    def test_zero(self):
        self.assertEqual(subtract(5, 0), 4, "Should return 4")

    def test_mixed_numbers(self):
        self.assertEqual(subtract(-5, 2), -8, "Should return -8")

    def test_mixed_numbers2(self):
        self.assertEqual(subtract(5, -2), 6, "Should return 6")


if __name__ == '__main__':
    unittest.main()