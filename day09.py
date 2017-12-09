"""
http://adventofcode.com/2017/day/9
"""

import pytest


def unbanged_chars(stream):
    chars = iter(stream)
    while True:
        ch = next(chars)
        if ch == '!':
            next(chars)
        else:
            yield ch

def score(stream):
    total = 0
    depth = 0
    garbage = False
    for ch in unbanged_chars(stream):
        if garbage:
            if ch == '>':
                garbage = False
        else:
            if ch == '{':
                depth += 1
            elif ch == '}':
                total += depth
                depth -= 1
            elif ch == '<':
                garbage = True
    return total

@pytest.mark.parametrize("stream, answer", [
    ("{}", 1),
    ("{{{}}}", 6),
    ("{{},{}}", 5),
    ("{{{},{},{{}}}}", 16),
    ("{<a>,<a>,<a>,<a>}", 1),
    ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
    ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
    ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
])
def test_score(stream, answer):
    assert score(stream) == answer


if __name__ == '__main__':
    with open("day09_input.txt") as finput:
        stream = finput.read()
    print(f"Part 1: total score is {score(stream)}")
