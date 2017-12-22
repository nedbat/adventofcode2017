"""
http://adventofcode.com/2017/day/22
"""

from collections import defaultdict
from enum import Enum

import pytest

# The grid is a dict mapping coordinates to state

class State(Enum):
    CLEAN = 1
    WEAKENED = 2
    INFECTED = 3
    FLAGGED = 4


def read_grid(lines):
    """Return a dict of infected points, and the coords of the center."""
    grid = defaultdict(lambda: State.CLEAN)
    width = None
    for y, line in enumerate(lines):
        if width is None:
            width = len(line.strip())
        for x, ch in enumerate(line):
            if ch == '#':
                grid[(x, y)] = State.INFECTED

    center = (width // 2, y // 2)
    return grid, center


def test_read_grid():
    with open("day22_input.txt") as finput:
        grid, center = read_grid(finput)
    assert len(grid) == 292
    assert center == (12, 12)


DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]

RIGHT = {d1: d2 for d1, d2 in zip(DIRS, DIRS[1:])}
LEFT = {d2: d1 for d1, d2 in zip(DIRS, DIRS[1:])}
REVERSE = {d: (-d[0], -d[1]) for d in DIRS}
STRAIGHT = {d: d for d in DIRS}

class Virus1:
    def __init__(self, grid, pos):
        self.grid = grid
        self.pos = pos
        self.direction = (0, -1)
        self.infections = 0

    def step(self):
        if self.grid[self.pos] == State.INFECTED:
            # This is infected
            turns = RIGHT
            new_state = State.CLEAN
            del self.grid[self.pos]
        else:
            turns = LEFT
            new_state = State.INFECTED
            self.infections += 1
        self.grid[self.pos] = new_state
        self.direction = turns[self.direction]
        self.advance()

    def advance(self):
        self.pos = (
            self.pos[0] + self.direction[0],
            self.pos[1] + self.direction[1]
            )

def infections_after_steps(lines, steps, virus_class=Virus1):
    grid, center = read_grid(lines)
    virus = virus_class(grid, center)
    for _ in range(steps):
        virus.step()
    return virus.infections

TEST_INPUT = ["..#","#..","..."]

def test_infections_after_steps():
    infections = infections_after_steps(TEST_INPUT, 10_000)
    assert infections == 5587


if __name__ == '__main__':
    with open("day22_input.txt") as finput:
        infections = infections_after_steps(finput, 10_000)
    print(f"Part 1: after 10,000 steps, {infections} bursts caused an infection.")


class Virus2(Virus1):
    def step(self):
        state = self.grid[self.pos]
        if state == State.CLEAN:
            turns = LEFT
            new_state = State.WEAKENED
        elif state == State.WEAKENED:
            turns = STRAIGHT
            new_state = State.INFECTED
            self.infections += 1
        elif state == State.INFECTED:
            turns = RIGHT
            new_state = State.FLAGGED
        else:
            assert state == State.FLAGGED
            turns = REVERSE
            new_state = State.CLEAN
        self.grid[self.pos] = new_state
        self.direction = turns[self.direction]
        self.advance()

@pytest.mark.parametrize("steps, infections", [
    (100, 26),
    (10_000_000, 2511944),
])
def test_infections_after_steps2(steps, infections):
    actual = infections_after_steps(TEST_INPUT, steps, Virus2)
    assert actual == infections


if __name__ == '__main__':
    with open("day22_input.txt") as finput:
        infections = infections_after_steps(finput, 10_000_000, Virus2)
    print(f"Part 2: after 10,000,000 steps, {infections} bursts caused an infection.")
