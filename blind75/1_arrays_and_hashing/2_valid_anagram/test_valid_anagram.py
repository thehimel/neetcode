"""Author: Himel Das"""

import pytest
from valid_anagram import is_anagram, is_anagram_sorted
from valid_anagram_optimized import is_anagram_optimized


@pytest.mark.parametrize("test_input, expected", [
    (("anagram", "nagaram"), True), (("rat", "car"), False), (("moon", "nom"), False)])
def test_is_anagram(test_input, expected):
    assert is_anagram(*test_input) == expected
    assert is_anagram_sorted(*test_input) == expected
    assert is_anagram_optimized(*test_input) == expected
