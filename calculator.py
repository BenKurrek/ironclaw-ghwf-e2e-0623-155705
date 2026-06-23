"""A tiny calculator module.

The contract is documented in each function's docstring. The test suite in
``test_calculator.py`` pins the expected behavior.
"""


def add(a, b):
    """Return the sum of ``a`` and ``b``."""
    return a + b


def average(numbers):
    """Return the arithmetic mean of a non-empty list of numbers.

    The arithmetic mean is the sum of the values divided by the *count of
    values*. For example, ``average([2, 4, 6])`` must return ``4.0``.

    Raises:
        ValueError: if ``numbers`` is empty.
    """
    if not numbers:
        raise ValueError("average() requires a non-empty list")

    total = 0
    for n in numbers:
        total += n

    return total / len(numbers)
