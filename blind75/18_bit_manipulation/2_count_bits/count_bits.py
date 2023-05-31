"""
338. Counting Bits
https://leetcode.com/problems/counting-bits/description/
Note: Optimized version available.
"""


def get_count(n: int) -> int:
    """
    Author: Himel Das
    Calculate the number of 1's in an integer.
    """
    res = 0
    while n:
        res += n % 2  # If the right most element of n is 1, n % 2 = 1, else 0.
        n //= 2
    return res


def count_bits(n: int) -> list[int]:
    """
    Author: Himel Das
    TC: O(NLog(N)) because the TC for finding the count of 1's for an integer is Log(N).
    SC: O(N)
    """
    res = []
    for i in range(n + 1):
        res.append(get_count(i))
    return res
