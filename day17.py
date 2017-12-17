"""
http://adventofcode.com/2017/day/17
"""

def spin(steps):
    buffer = [0]
    pos = 0
    value = 1
    while value < 2018:
        # Step forward steps times
        pos = (pos + steps + 1) % len(buffer)
        buffer.insert(pos, value)
        value += 1
    return buffer[pos+1]


def test_spin():
    assert spin(3) == 638

INPUT = 345

if __name__ == '__main__':
    value = spin(INPUT)
    print(f"Part 1: the value after 2017 is {value}")
