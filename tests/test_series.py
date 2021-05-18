
print('hello world')
import pytest
from math_series.series import hello

def test_one():
    actual = hello()
    expected = 'hello world'
    assert actual == expected
test_one()