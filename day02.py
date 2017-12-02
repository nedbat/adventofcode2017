"""
http://adventofcode.com/2017/day/2
"""

data = """
    5 1 9 5
    7 5 3
    2 4 6 8
    """

data_lines = data.strip().splitlines()

def read_sheet(lines):
    return [[int(cell) for cell in row.split()] for row in lines]

def test_read_sheet():
    assert read_sheet(data_lines) == [[5,1,9,5], [7,5,3], [2,4,6,8]]

def checksum(sheet):
    return sum(max(row) - min(row) for row in sheet)

def test_checksum():
    assert checksum(read_sheet(data_lines)) == 18

if __name__ == '__main__':
    sheet = read_sheet(open("day02_input.txt"))
    print(f"Puzzle 1: checksum is {checksum(sheet)}")