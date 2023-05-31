"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
"""


def longest_consecutive(nums: list[int]) -> int:
    """
    Author: Neetcode
    TC: O(N)
    SC: O(N)
    """
    num_set = set(nums)
    longest = 0

    for n in nums:
        # check if it is the start of a sequence
        if n-1 not in num_set:
            length = 0
            while n+length in num_set:
                length += 1
            longest = max(length, longest)
    return longest
