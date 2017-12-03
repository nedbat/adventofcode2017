"""
http://adventofcode.com/2017/day/3
"""

import itertools
import math

import pytest


def ring_of(n):
    if n == 1:
        return 0
    ring = int(math.sqrt(n-1))
    if ring % 2 == 0:
        ring -= 1
    ring //= 2
    ring += 1
    return ring

@pytest.mark.parametrize("n, ring", [
    (1, 0),
    (2, 1),
    (9, 1),
    (10, 2),
    (12, 2),
    (23, 2),
    (24, 2),
    (25, 2),
    (26, 3),
])
def test_ring_of(n, ring):
    assert ring_of(n) == ring


def location_of(n):
    """Return the x,y coords of n in the infinite memory grid."""
    if n == 1:
        return 0, 0
    ring = ring_of(n)
    side = ring * 2
    start = (2 * ring - 1) ** 2 + 1
    offset = n - start
    which_side = offset // side
    place_in_side = offset - (which_side * side)
    if which_side == 0:
        return ring, place_in_side - (ring - 1)
    elif which_side == 1:
        return (ring - 1) - place_in_side, ring
    elif which_side == 2:
        return -ring, (ring - 1) - place_in_side
    elif which_side == 3:
        return place_in_side - (ring - 1), -ring
    else:
        assert False

@pytest.mark.parametrize("n, coords", [
    (1, (0, 0)),
    (12, (2, 1)),
    (23, (0, -2)),
])
def test_location_of(n, coords):
    assert location_of(n) == coords


def distance_to_port(n):
    x, y = location_of(n)
    return abs(x) + abs(y)

@pytest.mark.parametrize("n, dist", [
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31),
])
def test_distance_to_port(n, dist):
    assert distance_to_port(n) == dist

INPUT = 289326

if __name__ == '__main__':
    print(f"Part 1: the distance to {INPUT} is {distance_to_port(INPUT)}")


# Part 2: completely different solution! :)

def neighbors(x, y):
    """Produce coordinates of neighbors."""
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx or dy:
                yield x + dx, y + dy


class MemoryGrid:
    def __init__(self):
        # Maps tuples of coordinates to values.
        self.cells = {}

    def sum_of_neighbors(self, x, y):
        return sum(self.cells.get((nx, ny), 0) for nx, ny in neighbors(x, y))

    def stress_fill(self):
        self.cells[(0, 0)] = 1
        yield 1
        for n in itertools.count(start=2):
            x, y = location_of(n)
            self.cells[(x, y)] = val = self.sum_of_neighbors(x, y)
            yield val

def test_stress_fill():
    grid = MemoryGrid()
    result = [1, 1, 2, 4, 5, 10, 11, 23, 25, 26, 54, 57, 59, 122, 133, 142, 147, 304, 330, 351, 362, 747, 806]
    assert list(itertools.islice(grid.stress_fill(), len(result))) == result


if __name__ == '__main__':
    grid = MemoryGrid()
    answer = next(itertools.dropwhile(lambda v: v < INPUT, grid.stress_fill()))
    print(f"Part 2: the first value more than {INPUT} is {answer}")
