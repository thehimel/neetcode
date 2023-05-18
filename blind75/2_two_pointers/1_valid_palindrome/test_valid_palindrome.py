"""
Author: Himel Das
"""

import pytest
from valid_palindrome import is_palindrome


@pytest.mark.parametrize("test_input, expected", [
    ("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True)])
def test_contains_duplicate(test_input, expected):
    assert is_palindrome(test_input) == expected
