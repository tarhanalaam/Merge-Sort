# Merge-Sort

*Cause bubble sort sucks.*

A simple, from-scratch Python implementation of the merge sort algorithm, with basic timing benchmarks on sample integer and float datasets.

## How it works

`main.py` implements the classic divide-and-conquer merge sort:

1. **`merge_sort(arr)`** — recursively splits the input list in half until each sublist has 0 or 1 elements (the base case, which is already sorted).
2. **`merge(first, second)`** — merges two already-sorted lists into a single sorted list by repeatedly comparing the front elements of each and appending the smaller one, then appending any leftovers once one list is exhausted.

Running the script sorts two sample datasets defined in `test_cases.py` (a list of integers and a list of floats) and prints how long each sort took.

## Requirements

- Python (version pinned in `.python-version`)
- [uv](https://docs.astral.sh/uv/) (recommended) — the project ships a `pyproject.toml` and `uv.lock`

No external dependencies are required beyond the standard library.

## Usage

With `uv`:

```bash
uv run main.py
```

Or with plain Python:

```bash
python main.py
```

### Example output

```
[3, 4, 7, 9, 11, 12, 15, 27, 42, 46, 55, 63, 78, 89, 91, 134, 156, 200, 218, 300]
First run took: 0.00001 seconds
[0.577, 0.693, 1.202, 1.381, 1.414, 1.618, 1.732, 2.236, 2.502, 2.718, 3.14, 3.674, 4.669, 5.291, 6.022, 6.674, 7.389, 8.314, 9.109, 9.81]
Second run took: 0.00001 seconds
```

## Project structure

```
.
├── main.py           # merge_sort / merge implementation + timing benchmark
├── test_cases.py      # sample integer and float lists used by main.py
├── pyproject.toml     # project metadata
├── uv.lock             # locked dependency versions (for uv)
└── .python-version     # pinned Python version
```

## Complexity

Merge sort runs in **O(n log n)** time in all cases (best, average, and worst), at the cost of **O(n)** additional space for the temporary sublists — a solid, predictable alternative to O(n²) algorithms like bubble sort.