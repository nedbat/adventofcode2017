import pytest


class Circle:
    def __init__(self, lst):
        self.lst = lst

    def _circleslice(self, slice):
        """Return two start,stop pairs"""
        start = slice.start % len(self.lst)
        stop = slice.stop % len(self.lst)
        if slice.start == slice.stop:
            return start, stop, None, None
        if start < stop:
            return start, stop, None, None
        else:
            return start, len(self.lst), 0, stop

    def __getitem__(self, slice):
        s1, e1, s2, e2 = self._circleslice(slice)
        val = self.lst[s1:e1]
        if s2 is not None:
            val += self.lst[s2:e2]
        return val

    def __setitem__(self, slice, value):
        s1, e1, s2, e2 = self._circleslice(slice)
        value = list(value)
        self.lst[s1:e1] = value[:(e1 - s1)]
        if s2 is not None:
            self.lst[s2:e2] = value[(e1 - s1):]


@pytest.mark.parametrize("start, stop, result", [
    (3, 9, [3, 4, 5, 6, 7, 8]),
    (8, 12, [8, 9, 0, 1]),
    (0, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
])
def test_get(start, stop, result):
    assert Circle(list(range(10)))[start:stop] == result

@pytest.mark.parametrize("start, stop, length, result", [
    (3, 9, 6, [0, 1, 2, 100, 101, 102, 103, 104, 105, 9]),
    (8, 12, 4, [102, 103, 2, 3, 4, 5, 6, 7, 100, 101]),
])
def test_set(start, stop, length, result):
    lst = list(range(10))
    circle = Circle(lst)
    circle[start:stop] = range(100, 100+length)
    assert lst == result


def knot_hash(data, lengths):
    circle = Circle(data)
    pos = 0
    skip = 0
    for length in lengths:
        circle[pos:pos+length] = reversed(circle[pos:pos+length])
        pos += length + skip
        skip += 1


def test_knot_hash():
    data = list(range(5))
    knot_hash(data, [3, 4, 1, 5])
    assert data == [3, 4, 2, 1, 0]


if __name__ == '__main__':
    INPUT = list(map(int, "97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190".split(",")))
    data = list(range(256))
    knot_hash(data, INPUT)
    result = data[0] * data[1]
    print(f"Part 1: multiplying the first two numbers gives {result}")
