import pytest
from contains_duplicate import contains_duplicate


@pytest.mark.parametrize("test_input, expected", [
    ([1, 2, 3, 1], True), ([1, 2, 3, 4], False), ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)])
def test_contains_duplicate(test_input, expected):
    assert contains_duplicate(test_input) == expected
