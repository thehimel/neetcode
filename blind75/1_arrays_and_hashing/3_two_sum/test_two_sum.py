"""Author: Himel Das"""

import pytest
from two_sum import two_sum


@pytest.mark.parametrize("test_input, expected", [
    (([2, 7, 11, 15], 9), [0, 1]), (([3, 2, 4], 6), [1, 2]), (([3, 3], 6), [0, 1])])
def test_two_sum(test_input, expected):
    assert two_sum(*test_input) == expected
