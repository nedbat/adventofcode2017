"""
http://adventofcode.com/2017/day/2
"""

import itertools

import pytest


DATA_LINES = """
    5 1 9 5
    7 5 3
    2 4 6 8
    """.strip().splitlines()

def read_sheet(lines):
    return [[int(cell) for cell in row.split()] for row in lines]

def test_read_sheet():
    assert read_sheet(DATA_LINES) == [[5,1,9,5], [7,5,3], [2,4,6,8]]

def checksum(sheet):
    return sum(max(row) - min(row) for row in sheet)

def test_checksum():
    assert checksum(read_sheet(DATA_LINES)) == 18

if __name__ == '__main__':
    sheet = read_sheet(open("day02_input.txt"))
    print(f"Part 1: checksum is {checksum(sheet)}")

# Part 2

def divisible_pairs(nums):
    for a, b in itertools.product(nums, nums):
        if a == b:
            continue
        if a % b == 0:
            yield a, b

@pytest.mark.parametrize("nums, result", [
    ([5, 9, 2, 8], [(8, 2)]),
    ([9, 4, 7, 3], [(9, 3)]),
    ([3, 8, 6, 5], [(6, 3)]),
])
def test_divisible_pairs(nums, result):
    assert list(divisible_pairs(nums)) == result

DATA_LINES_2 = """
    5 9 2 8
    9 4 7 3
    3 8 6 5
    """.strip().splitlines()

def checksum2(sheet):
    check = 0
    for row in sheet:
        for num, denom in divisible_pairs(row):
            check += num // denom
    return check

def test_checksum2():
    assert checksum2(read_sheet(DATA_LINES_2)) == 9

if __name__ == '__main__':
    sheet = read_sheet(open("day02_input.txt"))
    print(f"Part 2: sum of divisible pairs is {checksum2(sheet)}")
