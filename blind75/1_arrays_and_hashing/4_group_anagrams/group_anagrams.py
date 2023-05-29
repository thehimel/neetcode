"""
49. Group Anagrams

https://leetcode.com/problems/group-anagrams/
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Author: Himel Das

    TC: O(M.NlogN) where NlogN is the TC for sorting each word, and M is the length of the input list.
    SC: O(N)
    """
    dictionary = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in dictionary:
            dictionary[sorted_word] = [word]
        else:
            dictionary[sorted_word].append(word)
    return list(dictionary.values())
