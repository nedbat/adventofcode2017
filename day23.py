"""
http://adventofcode.com/2017/day/23
"""

import collections

INPUT = """\
set b 79
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23
"""


class Processor:
    def __init__(self, instructions):
        self.registers = collections.defaultdict(int)
        self.instructions = [line.split() for line in instructions]
        self.pc = 0
        self.op_counts = collections.defaultdict(int)

    def __getitem__(self, arg):
        try:
            return int(arg)
        except ValueError:
            return self.registers[arg]

    def __setitem__(self, name, value):
        self.registers[name] = value

    def op_set(self, x, y):
        self[x] = self[y]

    def op_sub(self, x, y):
        self[x] -= self[y]

    def op_mul(self, x, y):
        self[x] *= self[y]

    def op_jnz(self, x, y):
        if self[x] != 0:
            return self[y]

    def one_step(self):
        if not(0 <= self.pc < len(self.instructions)):
            return False
        op, *args = self.instructions[self.pc]
        self.op_counts[op] += 1
        func = getattr(self, f"op_{op}")
        pc_delta = func(*args)
        self.pc += pc_delta if pc_delta is not None else 1
        return True

if __name__ == '__main__':
    proc = Processor(INPUT.splitlines())
    while proc.one_step():
        pass
    print(proc.op_counts)
    print(f"Part 1: mul has been executed {proc.op_counts['mul']} times.")
