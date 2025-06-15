# Test strategy:
# We will use the unittest framework to test the two_sum function.
# The tests will cover the following scenarios:
# 1. Basic test cases with positive and negative integers.
# 2. Test cases with zero values.
# 3. Test cases with duplicate numbers in the input list.
# 4. Test cases where the target is not found.
# 5. Test cases with an empty input list.
# 6. Test cases with a list containing only one element.
# Bug Regression:
# If a bug is found, a new test case will be added to specifically target that bug.
# The test case will fail if the bug is still present.
# This ensures that the bug is not reintroduced in future releases.

import unittest
from two_sum import two_sum  # Assuming the function is in two_sum.py

class TestTwoSum(unittest.TestCase):

    def test_basic_positive(self):
        """Test case with positive integers."""
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertEqual(two_sum(nums, target), expected)

    def test_basic_negative(self):
        """Test case with negative integers."""
        nums = [-1, -3, 2, 5]
        target = 1
        expected = [0, 2]
        self.assertEqual(two_sum(nums, target), expected)

    def test_zero_values(self):
        """Test case with zero values."""
        nums = [0, 4, 3, 0]
        target = 0
        expected = [0, 3]
        self.assertEqual(two_sum(nums, target))

    def test_duplicate_numbers(self):
        """Test case with duplicate numbers."""
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertEqual(two_sum(nums, target), expected)

    def test_target_not_found(self):
        """Test case where the target is not found."""
        nums = [1, 2, 3]
        target = 10
        expected = None
        self.assertEqual(two_sum(nums, target), None) # Changed assertion to check for None

    def test_empty_list(self):
        """Test case with an empty input list."""
        nums = []
        target = 5
        expected = None
        self.assertEqual(two_sum(nums, target), None) # Changed assertion to check for None

    def test_single_element_list(self):
        """Test case with a list containing only one element."""
        nums = [5]
        target = 5
        expected = None
        self.assertEqual(two_sum(nums, target), None) # Changed assertion to check for None

    def test_negative_target(self):
        """Test case with a negative target value."""
        nums = [10, -5, 3]
        target = 5
        expected = [0, 1]
        self.assertEqual(two_sum(nums, target), [0,1])

    # Bug Regression Test (Example - Assume a previous bug where large numbers caused issues)
    def test_large_numbers(self):
        """Bug regression test for handling large numbers."""
        nums = [1000000000, 7]
        target = 1000000007
        expected = [0, 1]
        self.assertEqual(two_sum(nums, target), expected)

    # Bug Regression Test (Example - Assume a bug where indices were returned out of order)
    def test_indices_order(self):
        """Bug regression test to ensure indices are returned in the correct order (smaller index first)."""
        nums = [4,2,11,3]
        target = 6
        expected = [1,3]
        self.assertEqual(two_sum(nums, target), [1,3])

if __name__ == '__main__':
    # Example Usage (Optional - Can be removed when running tests with a test runner)
    unittest.main()