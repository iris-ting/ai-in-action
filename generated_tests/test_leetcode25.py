# Test strategy:
# We will use the unittest framework to test the is_valid function.
# The test cases will cover the following scenarios:
# 1. Empty string: Should return True.
# 2. Valid parentheses: Should return True.
# 3. Invalid parentheses: Should return False.
# 4. Only opening parentheses: Should return False.
# 5. Only closing parentheses: Should return False.
# 6. Mixed valid parentheses: Should return True.
# 7. Mixed invalid parentheses: Should return False.
# 8. Invalid characters: Should return False.
#
# Bug Regression:
# This test suite includes test cases that specifically target potential bugs,
# such as mismatched parentheses types or handling invalid characters.
# In the event a bug is identified, a new test case is added or an existing one is modified to reproduce the bug consistently.
# This helps ensure that the bug is not reintroduced in future code changes.

import unittest

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
        self.assertTrue(is_valid("()[]{}"))
        self.assertTrue(is_valid("{[]}"))

    def test_invalid_parentheses(self):
        self.assertFalse(is_valid("(]"))
        self.assertFalse(is_valid("([)]"))

    def test_only_opening_parentheses(self):
        self.assertFalse(is_valid("("))
        self.assertFalse(is_valid("[{("))

    def test_only_closing_parentheses(self):
        self.assertFalse(is_valid(")"))
        self.assertFalse(is_valid("}])"))

    def test_mixed_valid_parentheses(self):
        self.assertTrue(is_valid("(){}[]"))
        self.assertTrue(is_valid("({[]})"))
        self.assertTrue(is_valid("()[]{}"))

    def test_mixed_invalid_parentheses(self):
         self.assertFalse(is_valid("({[}])"))
         self.assertFalse(is_valid(")(}{]["))

    def test_invalid_characters(self):
        self.assertFalse(is_valid("a(b)c"))
        self.assertFalse(is_valid("(a)"))
        self.assertFalse(is_valid("[abc]"))
        self.assertFalse(is_valid("{123}"))

    def test_unclosed_parentheses(self):
        self.assertFalse(is_valid("((((("))
        self.assertFalse(is_valid("{{{{{"))
        self.assertFalse(is_valid("[[[[[["))
        self.assertFalse(is_valid("((()))))))"))

    def test_unopened_parentheses(self):
        self.assertFalse(is_valid(")))))"))
        self.assertFalse(is_valid("}}}}}"))
        self.assertFalse(is_valid("]]]]]"))
        self.assertFalse(is_valid("(((())))))"))


if __name__ == '__main__':
    unittest.main()