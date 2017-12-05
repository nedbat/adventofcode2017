"""
http://adventofcode.com/2017/day/5
"""

def do_jumps(jumps):
    jumps = list(jumps)
    steps = 0
    cur = 0

    while 0 <= cur < len(jumps):
        offset = jumps[cur]
        jumps[cur] += 1
        cur += offset
        steps += 1

    return steps

def test_do_jumps():
    assert do_jumps([0, 3, 0, 1, -3]) == 5

if __name__ == '__main__':
    with open('day05_input.txt') as finput:
        jumps = list(map(int, finput))
    steps = do_jumps(jumps)
    print(f"Part 1: escaped the maze in {steps} steps")


def do_jumps2(jumps):
    jumps = list(jumps)
    steps = 0
    cur = 0

    while 0 <= cur < len(jumps):
        offset = jumps[cur]
        if offset >= 3:
            jumps[cur] -= 1
        else:
            jumps[cur] += 1
        cur += offset
        steps += 1

    return steps

def test_do_jumps2():
    assert do_jumps2([0, 3, 0, 1, -3]) == 10

if __name__ == '__main__':
    with open('day05_input.txt') as finput:
        jumps = list(map(int, finput))
    steps = do_jumps2(jumps)
    print(f"Part 2: escaped the maze in {steps} steps")
