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


def adjacent_coordinates(pt):
    """What are the adjacent points on a 128-square grid?"""
    x, y = pt
    if x > 0:
        yield x - 1, y
    if x < 127:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < 127:
        yield x, y + 1


def adjacent_pairs(grid):
    """Produce all pairs of adjacent filled squares."""
    for pt1 in grid:
        for pt2 in adjacent_coordinates(pt1):
            if pt2 in grid:
                yield pt1, pt2

def grid_regions(grid):
    regions = {pt: {pt} for pt in grid}
    for pt1, pt2 in adjacent_pairs(grid):
        connected = regions[pt1] | regions[pt2]
        for p in connected:
            regions[p] = connected
    return regions

def count_regions(grid):
    regions = grid_regions(grid)
    regions_ids = set(id(r) for r in regions.values())
    return len(regions_ids)

def test_count_regions():
    grid = grid_from_key("flqrgnkx")
    assert count_regions(grid) == 1242


if __name__ == '__main__':
    grid = grid_from_key(INPUT)
    print(f"Part 2: there are {count_regions(grid)} regions.")
