"""Tests pinning the documented behavior of stats.py."""

import pytest

from stats import total, median


def test_total():
    assert total([1, 2, 3]) == 6


def test_median_odd():
    # sorted([3, 1, 2]) == [1, 2, 3]; the middle value is 2
    assert median([3, 1, 2]) == 2


def test_median_even():
    # sorted([1, 2, 3, 4]) == [1, 2, 3, 4]; the median is (2 + 3) / 2 == 2.5
    assert median([1, 2, 3, 4]) == 2.5


def test_median_empty_raises():
    with pytest.raises(ValueError):
        median([])
