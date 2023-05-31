"""
Author: Himel Das
"""

import pytest
from valid_palindrome import is_palindrome, is_palindrome_oneliner
from valid_palindrome_optimized import is_palindrome_optimized


@pytest.mark.parametrize("test_input, expected", [
    ("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True)])
def test_is_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected
    assert is_palindrome_oneliner(test_input) == expected
    assert is_palindrome_optimized(test_input) == expected
