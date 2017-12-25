"""
"""

BEGIN = 'A'
RUN_FOR = 12134527

PROGRAM = {
    ('A', 0): (1, 1, 'B'),
    ('A', 1): (0, -1, 'C'),
    ('B', 0): (1, -1, 'A'),
    ('B', 1): (1, 1, 'C'),
    ('C', 0): (1, 1, 'A'),
    ('C', 1): (0, -1, 'D'),
    ('D', 0): (1, -1, 'E'),
    ('D', 1): (1, -1, 'C'),
    ('E', 0): (1, 1, 'F'),
    ('E', 1): (1, 1, 'A'),
    ('F', 0): (1, 1, 'A'),
    ('F', 1): (1, 1, 'E'),
}

TEST_PROGRAM = {
    ('A', 0): (1, 1, 'B'),
    ('A', 1): (0, -1, 'B'),
    ('B', 0): (1, -1, 'A'),
    ('B', 1): (1, 1, 'A'),
}


class Machine:
    def __init__(self, program, start_state):
        self.tape = set()
        self.cursor = 0
        self.program = program
        self.state = start_state

    def step(self):
        one = int(bool(self.cursor in self.tape))
        write, move, new_state = self.program[self.state, one]
        if one and not write:
            self.tape.remove(self.cursor)
        elif write and not one:
            self.tape.add(self.cursor)
        self.cursor += move
        self.state = new_state

def tape_after_steps(program, steps):
    machine = Machine(program, 'A')
    for _ in range(steps):
        machine.step()
    return machine.tape

def test_machine():
    tape = tape_after_steps(TEST_PROGRAM, 6)
    assert len(tape) == 3


if __name__ == '__main__':
    tape = tape_after_steps(PROGRAM, RUN_FOR)
    checksum = len(tape)
    print(f"Part 1: checksum is {checksum}")
