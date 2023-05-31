"""
Author: Himel Das
"""

import pytest
from hamming_weight import hamming_weight, hamming_weight_optimized


@pytest.mark.parametrize("test_input, expected", [
    (0o00000000000000000000000000001011, 3),
    (0o00000000000000000000000010000000, 1),
    (0o11111111111111111111111111111101, 31)])
def test_is_palindrome(test_input, expected):
    assert hamming_weight(test_input) == expected
    assert hamming_weight_optimized(test_input) == expected
