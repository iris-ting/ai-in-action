# Test strategy:
# 1.  Basic positive numbers: Tests the subtraction of two positive integers.
# 2.  Negative numbers: Tests the subtraction of two negative integers, and a positive from a negative, and a negative from a positive.
# 3.  Zero: Tests subtraction with zero as one or both operands.
# 4.  Floating-point numbers: Tests subtraction of floating-point numbers, including cases with potential rounding errors.
# 5.  Large numbers: Tests subtraction with large numbers to ensure no overflow issues.
# 6.  Bug Regression:  (Assuming a bug was reported where subtracting a larger number from a smaller number resulted in a positive number - a typical integer overflow in languages without automatic large integer support, which is handled automatically in python)
#       - Test the scenario where y > x and assert that the result is negative.
#       - Added another test case specifically to check for the previous negative result.

import unittest
from subtract import subtract


class TestSubtract(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 5), 5)

    def test_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-10, -5), -5)
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(-5, 3), -8)

    def test_zero(self):
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_floating_point_numbers(self):
        self.assertAlmostEqual(subtract(5.5, 3.2), 2.3)
        self.assertAlmostEqual(subtract(10.7, 5.1), 5.6)
        self.assertAlmostEqual(subtract(1.0, 0.1), 0.9)  # Check for floating-point precision

    def test_large_numbers(self):
        self.assertEqual(subtract(1000000000, 1), 999999999)
        self.assertEqual(subtract(1000000000000, 500000000000), 500000000000)

    def test_bug_regression_negative_result(self):
        # This tests the bug where subtracting a larger number from a smaller number
        # resulted in a positive value.
        self.assertLess(subtract(3, 5), 0)
        self.assertEqual(subtract(1,2), -1)

if __name__ == '__main__':
    unittest.main()