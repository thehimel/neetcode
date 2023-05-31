"""
338. Counting Bits
https://leetcode.com/problems/counting-bits/description/
"""


def count_bits_optimized(n: int) -> list[int]:
    """
    Author: Neetcode
    TC: O(N)
    SC: O(N)
    """
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp
