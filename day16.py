"""
http://adventofcode.com/2017/day/16
"""

import pytest


def step_s(s, size):
    return s[-size:] + s[:-size]

def step_x(s, a, b):
    if a > b:
        a, b = b, a
    return s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]

def step_p(s, a, b):
    return step_x(s, s.index(a), s.index(b))

@pytest.mark.parametrize("s, size, answer", [
    ("abcde", 1, "eabcd"),
    ("abcde", 4, "bcdea"),
])
def test_step_s(s, size, answer):
    assert step_s(s, size) == answer

@pytest.mark.parametrize("s, a, b, answer", [
    ("eabcd", 3, 4, "eabdc"),
    ("abcde", 0, 4, "ebcda"),
])
def test_step_x(s, a, b, answer):
    assert step_x(s, a, b) == answer

@pytest.mark.parametrize("s, a, b, answer", [
    ("eabdc", "e", "b", "baedc"),
])
def test_step_p(s, a, b, answer):
    assert step_p(s, a, b) == answer


def try_int(s):
    try:
        return int(s)
    except ValueError:
        return s

def run_steps(steps, s):
    for step in steps.split(","):
        op = step[0]
        args = map(try_int, step[1:].split("/"))
        func = globals()[f"step_{op}"]
        s = func(s, *args)
    return s

def test_run_steps():
    assert run_steps("s1,x3/4,pe/b", "abcde") == "baedc"


if __name__ == '__main__':
    with open("day16_input.txt") as finput:
        steps = finput.read()
    result = run_steps(steps, "abcdefghijklmnop")
    print(f"Part 1: the programs are in this order: {result}")
