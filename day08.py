"""
http://adventofcode.com/2017/day/8
"""

import collections
import operator
import re


TEST_DATA = """\
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""

CONDITIONS = {
    '<': operator.__lt__,
    '<=': operator.__le__,
    '>': operator.__gt__,
    '>=': operator.__ge__,
    '==': operator.__eq__,
    '!=': operator.__ne__,
}

def execute(lines):
    registers = collections.defaultdict(int)
    high_water = 0
    for line in lines:
        m = re.search(r"^(\w+) (\w+) (-?\d+) if (\w+) ([<>=!]+) (-?\d+)", line)
        if not m:
            raise ValueError(f"Couldn't parse {line!r}")
        target, op, amount, checked, condition, value = m.groups()
        amount = int(amount)
        value = int(value)
        if CONDITIONS[condition](registers[checked], value):
            if op == "dec":
                amount = -amount
            registers[target] += amount
            if registers[target] > high_water:
                high_water = registers[target]
    return registers, high_water

def max_result(lines):
    registers, high_water = execute(lines)
    return max(registers.values()), high_water

def test_max_result():
    assert max_result(TEST_DATA.splitlines()) == (1, 10)


if __name__ == '__main__':
    with open("day08_input.txt") as finput:
        result, high_water = max_result(finput)
    print(f"Part 1: the largest value is {result}")
    print(f"Part 2: the largest value ever was {high_water}")
