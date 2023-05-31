"""
Author: Himel Das
"""

import pytest
from product_except_self import product_except_self


@pytest.mark.parametrize("test_input, expected", [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])])
def test_product_except_self(test_input, expected):
    assert product_except_self(test_input) == expected
