"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
"""


def is_palindrome(s: str) -> bool:
    """
    Author: Himel Das
    TC: O(N)
    SC: O(N)
    """
    s = filter(lambda c: c.isalnum(), s)
    return s == s[::-1]
