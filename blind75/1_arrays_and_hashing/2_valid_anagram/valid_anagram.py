"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

See valid_anagram_optimized() for more optimized code.
"""


def get_count(word: str) -> dict:
    """Author: Himel Das"""
    dictionary = dict()
    for character in word:
        if character in dictionary:
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary


def is_anagram(s: str, t: str) -> bool:
    """
    Author: Himel Das
    SC: O(N)
    TC: O(N)
    """
    if len(s) != len(t):
        return False
    return get_count(s) == get_count(t)


def is_anagram_sorted(s: str, t: str) -> bool:
    """
    Author: Himel Das
    SC: O(NLog(N))
    TC: O(1)
    """
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
