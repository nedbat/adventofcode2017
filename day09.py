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

def process(stream):
    """Returns total_score, garbage_chars."""
    total = 0
    depth = 0
    garbage = False
    gchars = 0
    for ch in unbanged_chars(stream):
        if garbage:
            if ch == '>':
                garbage = False
            else:
                gchars += 1
        else:
            if ch == '{':
                depth += 1
            elif ch == '}':
                total += depth
                depth -= 1
            elif ch == '<':
                garbage = True
    return total, gchars


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
    assert process(stream)[0] == answer


@pytest.mark.parametrize("stream, answer", [
    ('<>', 0),
    ('<random characters>', 17),
    ('<<<<>', 3),
    ('<{!>}>', 2),
    ('<!!>', 0),
    ('<!!!>>', 0),
    ('<{o"i!a,<{i<a>', 10),
])
def test_garbage_chars(stream, answer):
    assert process(stream)[1] == answer


if __name__ == '__main__':
    with open("day09_input.txt") as finput:
        stream = finput.read()
    score, gchars = process(stream)
    print(f"Part 1: total score is {score}")
    print(f"Part 1: there are {gchars} non-canceled characters within the garbage")
