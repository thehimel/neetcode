"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
"""
from collections import defaultdict


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Author: Himel Das

    TC: O(NlogN), due to sorting.
    SC: O(N)
    """
    dictionary = defaultdict(int)
    for n in nums:
        dictionary[n] += 1
    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return list(sorted_dictionary.keys())[:k]
