"""
http://adventofcode.com/2017/day/18
"""

import collections

INPUT = """\
set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 622
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19
"""

TEST_INPUT = """\
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
"""

class RecoveredFrequency(Exception):
    pass

class Processor1:
    def __init__(self):
        self.registers = collections.defaultdict(int)
        self.last_sound = None

    def value(self, arg):
        try:
            return int(arg)
        except ValueError:
            return self.registers[arg]

    def op_snd(self, x):
        self.last_sound = self.value(x)

    def op_set(self, x, y):
        self.registers[x] = self.value(y)

    def op_add(self, x, y):
        self.registers[x] += self.value(y)

    def op_mul(self, x, y):
        self.registers[x] *= self.value(y)

    def op_mod(self, x, y):
        self.registers[x] %= self.value(y)

    def op_rcv(self, x):
        if self.value(x) != 0:
            raise RecoveredFrequency()

    def op_jgz(self, x, y):
        if self.value(x) > 0:
            return self.value(y)

    def run_program(self, instructions):
        instructions = [line.split() for line in instructions]
        pc = 0
        while True:
            op, *args = instructions[pc]
            func = getattr(self, f"op_{op}")
            try:
                next_pc = func(*args)
            except RecoveredFrequency:
                return self.last_sound
            if next_pc is not None:
                pc += next_pc
            else:
                pc += 1


def test_processor1():
    processor = Processor1()
    sound = processor.run_program(TEST_INPUT.splitlines())
    assert sound == 4


if __name__ == '__main__':
    processor = Processor1()
    sound = processor.run_program(INPUT.splitlines())
    print(f"Part 1: the recovered frequency is {sound}")


class Processor2:
    def __init__(self, instructions):
        self.registers = collections.defaultdict(int)
        self.instructions = [line.split() for line in instructions]
        self.pc = 0
        self.ready = True
        self.q = collections.deque()
        self.recipient = None
        self.num_sent = 0

    def value(self, arg):
        try:
            return int(arg)
        except ValueError:
            return self.registers[arg]

    def receive(self, value):
        self.q.append(value)
        self.ready = True

    def op_snd(self, x):
        self.recipient.receive(self.value(x))
        self.num_sent += 1

    def op_set(self, x, y):
        self.registers[x] = self.value(y)

    def op_add(self, x, y):
        self.registers[x] += self.value(y)

    def op_mul(self, x, y):
        self.registers[x] *= self.value(y)

    def op_mod(self, x, y):
        self.registers[x] %= self.value(y)

    def op_rcv(self, x):
        if self.q:
            self.registers[x] = self.q.popleft()
        else:
            self.ready = False

    def op_jgz(self, x, y):
        if self.value(x) > 0:
            return self.value(y)

    def one_step(self):
        op, *args = self.instructions[self.pc]
        func = getattr(self, f"op_{op}")
        pc_delta = func(*args)
        if self.ready:
            self.pc += pc_delta if pc_delta is not None else 1


def run_two(instructions):
    p0 = Processor2(instructions)
    p1 = Processor2(instructions)
    p0.recipient = p1
    p1.recipient = p0
    p0.registers['p'] = 0
    p1.registers['p'] = 1

    while True:
        if p0.ready:
            p0.one_step()
        elif p1.ready:
            p1.one_step()
        else:
            # deadlocked!
            return p1.num_sent

def test_run_two():
    assert run_two("snd 1;snd 2;snd p;rcv a;rcv b;rcv c;rcv d".split(";")) == 3


if __name__ == '__main__':
    sent = run_two(INPUT.splitlines())
    print(f"Part 2: program 1 sent {sent} values")
