"""Tests pinning the documented behavior of calculator.py."""

import pytest

from calculator import add, average


def test_add():
    assert add(2, 3) == 5


def test_average_basic():
    # mean of [2, 4, 6] is 12 / 3 == 4.0
    assert average([2, 4, 6]) == 4.0


def test_average_single_element():
    # mean of a single value is the value itself
    assert average([5]) == 5.0


def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])
