"""
http://adventofcode.com/2017/day/3
"""

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
