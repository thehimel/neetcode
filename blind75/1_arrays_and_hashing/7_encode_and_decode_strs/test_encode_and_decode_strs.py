"""
Author: Himel Das
"""

import pytest
from encode_and_decode_strs import encode, decode


@pytest.mark.parametrize("test_input, expected", [
    (["Hello", "World!", "2023"], "5#Hello6#World!4#2023")])
def test_encode(test_input, expected):
    assert encode(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    ("5#Hello6#World!4#2023", ["Hello", "World!", "2023"])])
def test_decode(test_input, expected):
    assert decode(test_input) == expected
