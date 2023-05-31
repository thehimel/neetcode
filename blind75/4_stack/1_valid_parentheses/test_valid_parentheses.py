"""
Author: Himel Das
"""

import pytest
from valid_parentheses import is_valid


@pytest.mark.parametrize("test_input, expected", [
    ("()", True), ("()[]{}", True), ("(]", False), (")]", False)])
def test_is_valid(test_input, expected):
    assert is_valid(test_input) == expected
