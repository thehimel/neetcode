"""
Author: Himel Das
"""

import pytest
from count_bits import count_bits
from count_bits_optimized import count_bits_optimized


@pytest.mark.parametrize("test_input, expected", [
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2])])
def test_count_bits(test_input, expected):
    assert count_bits(test_input) == expected
    assert count_bits_optimized(test_input) == expected
