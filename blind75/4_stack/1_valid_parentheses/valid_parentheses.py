"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Note: Try with 2 pointers.
"""


def is_valid(s: str) -> bool:
    """
    Author: Neetcode

    TC: O(N)
    SC: O(N)
    """
    if len(s) % 2 != 0:
        return False

    validity = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for c in s:
        if c in validity:
            if stack and stack[-1] == validity[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False
