"""
http://adventofcode.com/2017/day/17
"""

def spin_work(step, stop):
    buffer = [0]
    pos = 0
    value = 1
    while value <= stop:
        # Step forward steps times
        pos = (pos + step) % len(buffer) + 1
        buffer.insert(pos, value)
        value += 1
    return buffer, pos

def spin(step, stop):
    buffer, pos = spin_work(step, stop)
    return buffer[pos + 1]

def test_spin():
    assert spin(3, 2017) == 638

INPUT = 345

if __name__ == '__main__':
    value = spin(INPUT, 2017)
    print(f"Part 1: the value after 2017 is {value}")


def spin2(step, stop):
    pos = 0
    value = 1
    onevalue = None
    while value <= stop:
        pos = (pos + step) % value + 1
        if pos == 1:
            onevalue = value
        value += 1
    return onevalue

def test_spin2():
    buffer, _ = spin_work(3, 2017)
    onevalue = spin2(3, 2017)
    assert buffer[1] == onevalue


if __name__ == '__main__':
    value = spin2(INPUT, 50_000_000)
    print(f"Part 2: the value after 0 after 50M insertions is {value}")
