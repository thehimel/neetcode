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
    s = "".join(filter(str.isalnum, s)).lower()
    return s == s[::-1]
