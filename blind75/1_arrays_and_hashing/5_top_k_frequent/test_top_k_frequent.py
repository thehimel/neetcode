"""Author: Himel Das"""

import pytest
from top_k_frequent import top_k_frequent


@pytest.mark.parametrize("test_input, expected", [
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]), (([1], 1), [1]), (([-1, -1], 1), [-1])])
def test_contains_duplicate(test_input, expected):
    assert top_k_frequent(*test_input) == expected
