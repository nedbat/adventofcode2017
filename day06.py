"""
http://adventofcode.com/2017/day/6
"""

import pytest


def max_index(banks):
    """Which block is the largest? Break ties with first."""
    return banks.index(max(banks))

@pytest.mark.parametrize("banks, mi", [
    ([1, 2, 3, 4], 3),
    ([4, 3, 2, 1], 0),
    ([1, 4, 2, 3, 4, 1], 1),
])
def test_max_index(banks, mi):
    assert max_index(banks) == mi


def reallocate_once(banks):
    """Find largest bank and reallocate its blocks."""
    banks = list(banks)
    pos = max_index(banks)
    blocks = banks[pos]
    banks[pos] = 0
    while blocks:
        pos += 1
        pos %= len(banks)
        banks[pos] += 1
        blocks -= 1
    return banks

@pytest.mark.parametrize("before, after", [
    ([0, 2, 7, 0], [2, 4, 1, 2]),
])
def test_reallocate_once(before, after):
    assert reallocate_once(before) == after


def count_reallocations(banks):
    seen = set()
    seen.add(tuple(banks))
    while True:
        banks = reallocate_once(banks)
        tbanks = tuple(banks)
        if tbanks in seen:
            break
        seen.add(tbanks)
    return len(seen)

def test_count_reallocations():
    assert count_reallocations([0, 2, 7, 0]) == 5


INPUT = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"

if __name__ == '__main__':
    banks = list(map(int, INPUT.split()))
    steps = count_reallocations(banks)
    print(f"Part 1: saw a previous configuration after {steps} cycles")
