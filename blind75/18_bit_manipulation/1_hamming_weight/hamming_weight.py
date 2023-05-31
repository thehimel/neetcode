"""
191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/
"""


def hamming_weight(n: int) -> int:
    """
    Author: Neetcode
    TC: O(32) = O(1). Because there is 32 bits.
    SC: O(1)
    Con: The operation is executed for all 1's and 0's
    """
    res = 0
    while n:
        res += n % 2  # If the right most element of n is 1, n % 2 = 1, else 0.
        n = n >> 1  # Bitwise right shift
    return res


def hamming_weight_optimized(n: int) -> int:
    """
    Author: Neetcode
    TC: O(32) = O(1). Because there is 32 bits.
    SC: O(1)
    Con: The operation is executed only for 1's.
    """
    res = 0
    while n:
        n = n & n-1
        res += 1
    return res
