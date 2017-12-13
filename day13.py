"""
http://adventofcode.com/2017/day/13
"""

import itertools

TEST_LAYERS = [(0, 3), (1, 2), (4, 4), (6, 4)]

def catches(layers, n):
    for depth, rng in layers:
        if (n + depth) % (2 * (rng - 1)) == 0:
            yield depth, rng

def test_catches():
    assert list(catches(TEST_LAYERS, 0)) == [(0, 3), (6, 4)]


def severity(layers, n):
    return sum(d * r for d, r in catches(layers, n))

def test_severity():
    assert severity(TEST_LAYERS, 0) == 24

INPUT = [
    (0, 4),
    (1, 2),
    (2, 3),
    (4, 5),
    (6, 8),
    (8, 4),
    (10, 6),
    (12, 6),
    (14, 6),
    (16, 10),
    (18, 6),
    (20, 12),
    (22, 8),
    (24, 9),
    (26, 8),
    (28, 8),
    (30, 8),
    (32, 12),
    (34, 12),
    (36, 12),
    (38, 8),
    (40, 10),
    (42, 14),
    (44, 12),
    (46, 14),
    (48, 12),
    (50, 12),
    (52, 12),
    (54, 14),
    (56, 14),
    (58, 14),
    (60, 12),
    (62, 14),
    (64, 14),
    (68, 12),
    (70, 14),
    (74, 14),
    (76, 14),
    (78, 14),
    (80, 17),
    (82, 28),
    (84, 18),
    (86, 14),
]

if __name__ == '__main__':
    print(f"Part 1: the severity of the whole trip is {severity(INPUT, 0)}")


def safe_delay(layers):
    # Brute-force it...
    for delay in itertools.count():
        if not any(catches(layers, delay)):
            return delay

def test_safe_delay():
    assert safe_delay(TEST_LAYERS) == 10

if __name__ == '__main__':
    print(f"Part 2: the safe delay is {safe_delay(INPUT)}")
