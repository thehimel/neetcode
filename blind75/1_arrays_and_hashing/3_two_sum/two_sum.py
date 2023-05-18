"""
1. Two Sum

https://leetcode.com/problems/two-sum/description/
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Author: Himel Das
    TC: O(N)
    SC: O(N)
    """
    seen = dict()
    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            return [seen[difference], i]
        else:
            seen[num] = i
