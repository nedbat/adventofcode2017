"""
http://adventofcode.com/2017/day/14
"""

import itertools

import pytest

from day10 import full_knot_hash


def one_bits(n):
    """Where are the 1's in binary n, one's digit is 0th."""
    for bit in itertools.count():
        if n % 2:
            yield bit
        n >>= 1
        if n == 0:
            return

@pytest.mark.parametrize("n, bits", [
    (0, []),
    (1, [0]),
    (2, [1]),
    (0xF0a5, [0, 2, 5, 7, 12, 13, 14, 15]),
])
def test_one_bits(n, bits):
    assert list(one_bits(n)) == bits


def grid_from_key(key):
    """Returns a set of (x,y) coordinates of filled squares."""
    grid = set()
    for row in range(128):
        knot_hash = full_knot_hash(f"{key}-{row}")
        for one_bit in one_bits(int(knot_hash, 16)):
            grid.add((128 - one_bit, row))

    return grid

def test_grid_from_key():
    grid = grid_from_key("flqrgnkx")
    assert len(grid) == 8108


INPUT = "xlqgujun"

if __name__ == '__main__':
    grid = grid_from_key(INPUT)
    print(f"Part 1: {len(grid)} squares are used.")
