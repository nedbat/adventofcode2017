"""
http://adventofcode.com/2017/day/22
"""

# The grid is a set of infected points.

def read_grid(lines):
    """Return a set of infected points, and the coords of the center."""
    grid = set()
    width = None
    for y, line in enumerate(lines):
        if width is None:
            width = len(line.strip())
        for x, ch in enumerate(line):
            if ch == '#':
                grid.add((x, y))

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

class Virus:
    def __init__(self, grid, pos):
        self.grid = grid
        self.pos = pos
        self.direction = (0, -1)
        self.infections = 0

    def step(self):
        if self.pos in self.grid:
            # This is infected
            turns = RIGHT
            self.grid.remove(self.pos)
        else:
            turns = LEFT
            self.grid.add(self.pos)
            self.infections += 1
        self.direction = turns[self.direction]
        self.pos = (
            self.pos[0] + self.direction[0],
            self.pos[1] + self.direction[1]
            )

def infections_after_steps(lines, steps):
    grid, center = read_grid(lines)
    virus = Virus(grid, center)
    for _ in range(steps):
        virus.step()
    return virus.infections

def test_infections_after_steps():
    infections = infections_after_steps(["..#","#..","..."], 10_000)
    assert infections == 5587


if __name__ == '__main__':
    with open("day22_input.txt") as finput:
        infections = infections_after_steps(finput, 10_000)
    print(f"Part 1: after 10,000 steps, {infections} bursts caused an infection.")
