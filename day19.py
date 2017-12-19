"""
http://adventofcode.com/2017/day/19
"""

TEST_INPUT = """\
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""

def turns(posx, posy, dx, dy):
    if dx == 0:
        yield posx + 1, posy, 1, 0
        yield posx - 1, posy, -1, 0
    else:
        yield posx, posy + 1, 0, 1
        yield posx, posy - 1, 0, -1

def walk_diagram(diagram):
    diagram = list(diagram)
    diagram += [' ' * len(diagram[-1])]
    posx = diagram[0].find("|")
    posy = 0
    dx = 0
    dy = 1
    seen = ""
    steps = 0
    while True:
        c = diagram[posy][posx]
        if c == '+':
            # change direction
            for nposx, nposy, ndx, ndy in turns(posx, posy, dx, dy):
                if diagram[nposy][nposx] != ' ':
                    posx, posy, dx, dy = nposx, nposy, ndx, ndy
                    break
        elif c == ' ':
            # done
            return seen, steps
        else:
            if c not in '|-':
                seen += c
            posx += dx
            posy += dy
        steps += 1


def test_walk_diagram():
    assert walk_diagram(TEST_INPUT.splitlines()) == ('ABCDEF', 38)


if __name__ == '__main__':
    with open("day19_input.txt") as finput:
        diagram = finput.readlines()
    seen, steps = walk_diagram(diagram)
    print(f"Part 1: the packet sees the letters {seen}")
    print(f"Part 1: the packet takes {steps} steps")
