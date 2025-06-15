# Test strategy:
#
# We will use the unittest framework to test the subtract function.
#
# Test cases will include:
#   - Positive numbers
#   - Negative numbers
#   - Zero
#   - Mixed positive and negative numbers
#
# Bug Regression:
# If a bug is found in the subtract function and fixed, a new test case
# that specifically targets the bug will be added to this test suite.
# This ensures that the bug does not reappear in future versions of the code.
#
# Example:
# Assume a bug was found where the function returned incorrect output when subtracting a large number from a small number.
# A test case specifically to test this scenario would be added.

import unittest
from substract import substract  # Import the function to be tested

class TestSubstract(unittest.TestCase):

    def test_positive_numbers(self):
        """Test subtracting positive numbers."""
        self.assertEqual(substract(5, 2), 3)
        self.assertEqual(substract(10, 5), 5)
        self.assertEqual(substract(100, 1), 99)

    def test_negative_numbers(self):
        """Test subtracting negative numbers."""
        self.assertEqual(substract(-5, -2), -3)
        self.assertEqual(substract(-10, -5), -5)
        self.assertEqual(substract(-100, -1), -99)

    def test_zero(self):
        """Test subtracting zero."""
        self.assertEqual(substract(5, 0), 5)
        self.assertEqual(substract(0, 5), -5)
        self.assertEqual(substract(0, 0), 0)

    def test_mixed_numbers(self):
        """Test subtracting mixed positive and negative numbers."""
        self.assertEqual(substract(5, -2), 7)
        self.assertEqual(substract(-5, 2), -7)
        self.assertEqual(substract(10, -5), 15)
        self.assertEqual(substract(-10, 5), -15)

    def test_large_numbers(self):
        """Test subtracting large numbers."""
        self.assertEqual(substract(1000000, 1), 999999)
        self.assertEqual(substract(1, 1000000), -999999)


    # Example Bug Regression Test (if a bug was found when subtracting a large number from a small number)
    def test_bug_regression_large_small(self):
        """Regression test for bug where subtracting a large number from a small number produced incorrect result."""
        self.assertEqual(substract(10, 100), -90)


if __name__ == '__main__':
    unittest.main()