"""
Author: Himel Das
"""

import pytest
from top_k_frequent import top_k_frequent
from top_k_frequent_optimized import top_k_frequent_optimized


@pytest.mark.parametrize("test_input, expected", [
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    (([1, 2, 3, 4, 5, 6], 2), [1, 2]),
    (([2, 2, 2, 2, 2, 3, 4, 4, 6, 6], 3), [2, 4, 6]),
    (([1], 1), [1]),
    (([-1, -1], 1), [-1])])
def test_contains_duplicate(test_input, expected):
    assert top_k_frequent(*test_input) == expected
    assert top_k_frequent_optimized(*test_input) == expected
