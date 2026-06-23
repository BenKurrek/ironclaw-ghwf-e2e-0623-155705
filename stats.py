"""A tiny statistics module.

The contract is documented in each function's docstring. The test suite in
``test_stats.py`` pins the expected behavior.
"""


def total(numbers):
    """Return the sum of a list of numbers."""
    result = 0
    for n in numbers:
        result += n
    return result


def median(numbers):
    """Return the median of a non-empty list of numbers.

    The median is the middle value of the *sorted* values. For an even-length
    list it is the average of the two middle values. For example,
    ``median([3, 1, 2])`` must return ``2`` and ``median([1, 2, 3, 4])`` must
    return ``2.5``.

    Raises:
        ValueError: if ``numbers`` is empty.
    """
    if not numbers:
        raise ValueError("median() requires a non-empty list")

    ordered = sorted(numbers)
    count = len(ordered)
    middle = count // 2

    # BUG: this returns ``ordered[middle]`` unconditionally, which is wrong for
    # even-length lists (it should average the two middle values) and also
    # picks the wrong index after sorting for some inputs. The fix must handle
    # both the odd and even cases.
    return ordered[middle]
