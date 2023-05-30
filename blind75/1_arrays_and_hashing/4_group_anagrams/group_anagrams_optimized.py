"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
"""

from collections import defaultdict


def group_anagrams_optimized(strs: list[str]) -> list[list[str]]:
    """
    Author: Neetcode
    TC: O(N)
    SC: O(N)

    Note: See group_anagrams_optimized.log
    """
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26  # a ... z
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)  # List can not be used as key in a dictionary but tuple can be for immutability.
    return list(res.values())
