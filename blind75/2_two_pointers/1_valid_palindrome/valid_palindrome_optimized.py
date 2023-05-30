"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
"""


def is_alphanum(char: str) -> bool:
    """
    Author: Neetcode
    ASCII Table: https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
    """
    # The ord() function returns the ASCII value of the character.
    return (ord("A") <= ord(char) <= ord("Z") or
            ord("a") <= ord(char) <= ord("z") or
            ord("0") <= ord(char) <= ord("9"))


def is_palindrome_optimized(s: str) -> bool:
    """
    Author: Neetcode

    TC: O(N)
    SC: O(1)
    """

    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not is_alphanum(s[left]):
            left += 1
        while left < right and not is_alphanum(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
