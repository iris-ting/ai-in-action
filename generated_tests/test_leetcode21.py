# Test strategy:
# 1.  Basic Valid Cases: Cover strings with correctly nested parentheses.
# 2.  Basic Invalid Cases:  Cover strings with mismatched parentheses or incorrect order.
# 3.  Empty String: Test the empty string, which should be considered valid.
# 4.  Single Parenthesis: Test strings with a single opening or closing parenthesis, both invalid.
# 5.  Mixed Parentheses Types: Test strings with a mix of different types of parentheses.
# 6.  Unbalanced Parentheses: Test cases with more opening or closing parentheses of a specific type.
# 7.  Nested Parentheses:  Test deeply nested parentheses.
# 8.  Invalid characters: Test cases with invalid characters

# Bug Regression:
# - Test case "()" was added to ensure basic valid parentheses are handled correctly (regression test for a potential previous error where basic valid case was failing)
# - Test case "{[]}" was added to ensure multiple valid nested parentheses are handled correctly
# - Test case ")(" was added to ensure mis-matched parentheses are handled correctly.
# - Added invalid char test to catch edge cases where the program would crash.

import unittest

# from leetcode21 import is_valid  # Assuming the function is in a file named leetcode21.py

def is_valid(s: str) -> bool:
    """
    Returns True if the parentheses in the string are valid, otherwise False.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False  # invalid character

    return not stack


class TestValidParentheses(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_valid(""))

    def test_valid_parentheses(self):
        self.assertTrue(is_valid("()"))

    def test_valid_nested_parentheses(self):
        self.assertTrue(is_valid("(){}[]"))

    def test_valid_complex_nested_parentheses(self):
        self.assertTrue(is_valid("({[]})"))

    def test_invalid_parentheses(self):
        self.assertFalse(is_valid("(]"))

    def test_invalid_mismatched_parentheses(self):
        self.assertFalse(is_valid(")("))

    def test_invalid_unclosed_parentheses(self):
        self.assertFalse(is_valid("("))

    def test_invalid_unbalanced_parentheses(self):
        self.assertFalse(is_valid("{{"))

    def test_invalid_parentheses_order(self):
        self.assertFalse(is_valid("}{"))

    def test_valid_nested_multiple_types(self):
        self.assertTrue(is_valid("{[]}"))

    def test_string_with_invalid_character(self):
        self.assertFalse(is_valid("abc(def)ghi"))

    def test_string_with_only_invalid_character(self):
         self.assertFalse(is_valid("a"))

if __name__ == '__main__':
    unittest.main()