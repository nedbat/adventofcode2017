"""
http://adventofcode.com/2017/day/7
"""

import re


TEST = """\
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""

class Towers:
    def __init__(self):
        self.weights = {}
        self.supporting = {}

    def read(self, lines):
        for line in lines:
            m = re.search(r"^(\w+) \((\d+)\)(?: -> (.*))?$", line)
            if m:
                name, weight, supporting = m.groups()
                self.weights[name] = int(weight)
                if supporting:
                    self.supporting[name] = supporting.split(", ")

    def bottom_program(self):
        bottoms = set(name for name in self.weights if not any(name in v for v in self.supporting.values()))
        assert len(bottoms) == 1
        return bottoms.pop()


def test_bottom_program():
    towers = Towers()
    towers.read(TEST.splitlines())
    assert towers.bottom_program() == "tknk"


if __name__ == '__main__':
    with open("day07_input.txt") as finput:
        towers = Towers()
        towers.read(finput)

    bottom = towers.bottom_program()
    print(f"Part 1: the bottom program is {bottom}")
