"""
http://adventofcode.com/2017/day/11

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

is:

nw | n | X
---+---+---
sw |   | ne
---+---+---
 X | s | se

or

---+ n +---
nw +---+ ne
---+   +---
sw +---+ se
---+ s +---
"""

import pytest

MOVES = {
    'n': (0, 2),
    'ne': (1, 1),
    'se': (1, -1),
    's': (0, -2),
    'sw': (-1, -1),
    'nw': (-1, 1),
}

def move(pos, steps):
    x, y = pos
    for step in steps.split(","):
        dx, dy = MOVES[step]
        x += dx
        y += dy
    return x, y

@pytest.mark.parametrize("steps, finish", [
    ("ne,ne,ne", (3, 3)),
    ("ne,ne,sw,sw", (0, 0)),
    ("ne,ne,s,s", (2, -2)),
    ("se,sw,se,sw,sw", (-1, -5)),
])
def test_move(steps, finish):
    assert move((0, 0), steps) == finish


def steps_to(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    while (x1, y1) != (x2, y2):
        if y1 < y2:
            sy = "n"
        else:
            sy = "s"

        if x1 < x2:
            sx = "e"
        elif x1 > x2:
            sx = "w"
        else:
            sx = ""

        step = sy + sx
        x1, y1 = move((x1, y1), step)
        yield step

@pytest.mark.parametrize("steps, shorter", [
    ("ne,ne,ne", "ne,ne,ne"),
    ("ne,ne,sw,sw", ""),
    ("ne,ne,s,s", "se,se"),
    ("se,sw,se,sw,sw", "sw,s,s"),
])
def test_steps_to(steps, shorter):
    finish = move((0, 0), steps)
    assert ",".join(steps_to((0, 0), finish)) == shorter


if __name__ == '__main__':
    with open("day11_input.txt") as finput:
        steps = finput.read().strip()
    finish = move((0, 0), steps)
    direct = list(steps_to((0, 0), finish))
    print(f"Part 1: fewest step to {finish} is {len(direct)} steps.")
