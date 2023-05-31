"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
Note: Review
"""


def product_except_self(nums: list[int]) -> list[int]:
    """
    Author: Neetcode
    TC: O(N)
    SC: O(1) | Output array is not considered in SC.
    """
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res
