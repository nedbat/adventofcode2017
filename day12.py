"""
http://adventofcode.com/2017/day/12
"""

import collections


class Programs:
    def __init__(self):
        self.progs = collections.defaultdict(set)

    def __getitem__(self, key):
        return self.progs[key]

    def connect(self, p1, p2):
        """Record that p1 and p2 are connected."""
        connected = self.progs[p1] | self.progs[p2] | {p1, p2}
        for p in connected:
            self.progs[p] = connected

    def read(self, lines):
        for line in lines:
            from_prog, arrow, to_progs = line.strip().partition('<->')
            from_prog = int(from_prog)
            for to_prog in to_progs.split(','):
                to_prog = int(to_prog)
                self.connect(from_prog, to_prog)


def test_connect():
    progs = Programs()
    progs.read("""\
        0 <-> 2
        1 <-> 1
        2 <-> 0, 3, 4
        3 <-> 2, 4
        4 <-> 2, 3, 6
        5 <-> 6
        6 <-> 4, 5
        """.strip().splitlines())
    assert len(progs.progs[0]) == 6


if __name__ == '__main__':
    progs = Programs()
    with open("day12_input.txt") as finput:
        progs.read(finput)
    print(f"Part 1: the group with program ID 0 has {len(progs.progs[0])} programs.")
