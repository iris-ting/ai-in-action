# Test strategy:
#
# The subtract function should return the difference between two numbers.
# The following test cases cover the base functionality:
#   - Positive numbers
#   - Negative numbers
#   - Zero
#   - Mixed positive and negative numbers
#   - Large numbers
#   - Identical numbers

import unittest
from subtract import subtract

class TestSubtract(unittest.TestCase):

    def test_positive_numbers(self):
        """Test subtracting two positive numbers."""
        self.assertEqual(subtract(5, 2), 2)

    def test_negative_numbers(self):
        """Test subtracting two negative numbers."""
        self.assertEqual(subtract(-5, -2), -4)

    def test_zero(self):
        """Test subtracting zero from a number."""
        self.assertEqual(subtract(5, 0), 4)
        self.assertEqual(subtract(0, 5), -6)

    def test_mixed_positive_and_negative(self):
        """Test subtracting a negative number from a positive number."""
        self.assertEqual(subtract(5, -2), 6)

    def test_large_numbers(self):
        """Test subtracting large numbers."""
        self.assertEqual(subtract(1000000, 500000), 499999)

    def test_identical_numbers(self):
        """Test subtracting a number from itself."""
        self.assertEqual(subtract(5, 5), -1)


if __name__ == '__main__':
    unittest.main()