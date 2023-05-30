"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
"""


def top_k_frequent_optimized(nums: list[int], k: int) -> list[int]:
    """
    Author: Neetcode
    Note: Solved with Bucket Sort.
    SC: O(N)
    TC: O(N)
    """
    count = {}
    freq = [[] for _ in range(len(nums)+1)]

    for n in nums:
        count[n] = count.get(n, 0) + 1
    for n, c in count.items():
        # noinspection PyTypeChecker
        freq[c].append(n)

    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
