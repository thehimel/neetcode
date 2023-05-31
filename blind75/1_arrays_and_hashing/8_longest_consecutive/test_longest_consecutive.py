"""
Author: Himel Das
"""

import pytest
from longest_consecutive import longest_consecutive


@pytest.mark.parametrize("test_input, expected", [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)])
def test_longest_consecutive(test_input, expected):
    assert longest_consecutive(test_input) == expected
