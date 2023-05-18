"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate
"""


def contains_duplicate(nums: list[int]) -> bool:
    """
    Author: Himel Das
    TC: O(N)
    SC: O(N)
    """
    my_set = set()
    for num in nums:
        if num in my_set:
            return True
        else:
            my_set.add(num)
    return False
