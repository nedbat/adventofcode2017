"""
http://adventofcode.com/2017/day/15
"""

import itertools

import pytest

FACTOR_A = 16807
FACTOR_B = 48271
DIVISOR = 2147483647

def generator(start, factor, criterion=1):
    value = start
    while True:
        value = value * factor % DIVISOR
        if value % criterion == 0:
            yield value

TEST_A_START = 65
TEST_B_START = 8921

@pytest.mark.parametrize("start, factor, expected", [
    (TEST_A_START, FACTOR_A, [1092455, 1181022009, 245556042, 1744312007, 1352636452]),
    (TEST_B_START, FACTOR_B, [430625591, 1233683848, 1431495498, 137874439, 285222916]),
])
def test_generator(start, factor, expected):
    assert list(itertools.islice(generator(start, factor), len(expected))) == expected


def count_low16_matches(pairs):
    return sum(a & 0xFFFF == b & 0xFFFF for a, b in pairs)

def count_generator_matches(start_a, start_b):
    gen_a = generator(start_a, FACTOR_A)
    gen_b = generator(start_b, FACTOR_B)
    return count_low16_matches(itertools.islice(zip(gen_a, gen_b), 40_000_000))

def test_count_generator_matches():
    assert count_generator_matches(TEST_A_START, TEST_B_START) == 588

INPUT_A_START = 783
INPUT_B_START = 325

if __name__ == '__main__':
    num = count_generator_matches(INPUT_A_START, INPUT_B_START)
    print(f"Part 1: judge's final count is {num}")


def count_generator_matches_part2(start_a, start_b):
    gen_a = generator(start_a, FACTOR_A, criterion=4)
    gen_b = generator(start_b, FACTOR_B, criterion=8)
    return count_low16_matches(itertools.islice(zip(gen_a, gen_b), 5_000_000))

def test_count_generator_matches_part2():
    assert count_generator_matches_part2(TEST_A_START, TEST_B_START) == 309

if __name__ == '__main__':
    num = count_generator_matches_part2(INPUT_A_START, INPUT_B_START)
    print(f"Part 2: judge's final count is {num}")
