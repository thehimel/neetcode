"""
271. Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings/
"""


def encode(strs: list[str]) -> str:
    """
    Encodes a list of strings to a single string.
    Author: Neetcode
    """
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(s: str) -> list[str]:
    """
    Decodes a single string to a list of strings.
    Author: Neetcode
    """
    res, i = [], 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        start, end = j+1, j+1+length
        res.append(s[start:end])
        i = end
    return res
