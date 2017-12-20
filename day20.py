"""
http://adventofcode.com/2017/day/20
"""

import itertools
import re

import attr

@attr.s
class Xyz:
    x = attr.ib()
    y = attr.ib()
    z = attr.ib()

    def __add__(self, other):
        return Xyz(self.x + other.x, self.y + other.y, self.z + other.z)

    def __len__(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

@attr.s
class Pt:
    i = attr.ib()
    p = attr.ib()
    v = attr.ib()
    a = attr.ib()

    def update(self):
        self.v += self.a
        self.p += self.v

    @classmethod
    def parse(cls, i, line):
        xyz = r"<(-?\d+),(-?\d+),(-?\d+)>"
        m = re.match(f"p={xyz}, v={xyz}, a={xyz}", line)
        if m:
            px, py, pz, vx, vy, vz, ax, ay, az = map(int, m.groups())
            return Pt(i, Xyz(px, py, pz), Xyz(vx, vy, vz), Xyz(ax, ay, az))

def read_points(lines):
    return [Pt.parse(i, line) for i, line in enumerate(lines)]

def eventual_distance_key(pt):
    """The key to use when determining the long-term distance from 0."""
    return (len(pt.a), len(pt.v), len(pt.p))

def distance_key(pt):
    """The key to use when determining the current distance from 0."""
    return len(pt.p), pt.p.x, pt.p.y, pt.p.z

if __name__ == '__main__':
    with open("day20_input.txt") as finput:
        points = read_points(finput)
    closest = min(points, key=eventual_distance_key)
    print(f"Part 1: the point that stays closest to 0 is {closest}")

def in_order(points):
    """Are the points all in the order they will remain forever?"""
    return sorted(points, key=eventual_distance_key) == sorted(points, key=distance_key)

def remove_dups(seq, key):
    for _, g in itertools.groupby(seq, key=key):
        g = list(g)
        if len(g) == 1:
            yield g[0]


def run_collisions(points):
    steps = 0
    while not in_order(points):
        points.sort(key=distance_key)
        new_points = list(remove_dups(points, key=lambda pt: pt.p))
        if len(points) != len(new_points) or steps % 100 == 0:
            print(f"After {steps} steps, {len(new_points)} points")
        points = new_points
        for pt in points:
            pt.update()
        steps += 1
    return points

if __name__ == '__main__':
    with open("day20_input.txt") as finput:
        points = read_points(finput)
    points = run_collisions(points)
    print(f"Part 2: {len(points)} particles are left")
