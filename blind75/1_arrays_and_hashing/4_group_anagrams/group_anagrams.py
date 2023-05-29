"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
Note: Optimized version available.
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Author: Himel Das

    TC: O(M.NlogN)
        Here N is the length for each word, then NlogN is the TC for sorting each word.
        M is the length of the input list. We need to sort the words M times. Thus, total TC is O(M.NlogN).
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
