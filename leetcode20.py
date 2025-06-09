# LeetCode 20: Valid Parentheses
# test 3

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