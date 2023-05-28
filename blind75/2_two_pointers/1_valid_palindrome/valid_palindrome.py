"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

is_palindrome_optimized() is available.
"""


def is_palindrome(s: str) -> bool:
    """
    Author: Himel Das
    TC: O(N)
    SC: O(N)

    Cons: Uses extra memory.
    """
    sentence = ""
    for char in s:
        if char.isalnum():
            sentence += char.lower()
    return sentence == sentence[::-1]


def is_palindrome_oneliner(s: str) -> bool:
    """
    Author: Himel Das
    TC: O(N)
    SC: O(N)
    """
    s = "".join(filter(str.isalnum, s)).lower()
    return s == s[::-1]
