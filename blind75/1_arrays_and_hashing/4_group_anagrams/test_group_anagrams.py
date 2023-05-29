"""Author: Himel Das"""

import pytest
from group_anagrams import group_anagrams
from group_anagrams_optimized import group_anagrams_optimized


@pytest.mark.parametrize("test_input, expected", [
    (["eat", "tea", "tan", "ate", "nat", "bat"], [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
    ([""], [[""]]),
    (["a"], [["a"]])])
def test_contains_duplicate(test_input, expected):
    assert group_anagrams(test_input) == expected
    assert group_anagrams_optimized(test_input) == expected
