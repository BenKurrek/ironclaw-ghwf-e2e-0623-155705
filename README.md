# ironclaw-ghwf-e2e

A tiny calculator package used as a disposable fixture for an end-to-end test
of the IronClaw GitHub issue workflow.

## Modules

- `calculator.py` — `add(a, b)` and `average(numbers)`.

## Running the tests

```bash
pip install pytest
pytest -q
```

`test_average_basic` and `test_average_single_element` currently fail because
`average()` divides by `len(numbers) - 1` instead of `len(numbers)`. See the
open issue.
