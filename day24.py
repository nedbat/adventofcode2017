"""
http://adventofcode.com/2017/day/24
"""


TEST_INPUT = """\
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
"""

INPUT = """\
14/42
2/3
6/44
4/10
23/49
35/39
46/46
5/29
13/20
33/9
24/50
0/30
9/10
41/44
35/50
44/50
5/11
21/24
7/39
46/31
38/38
22/26
8/9
16/4
23/39
26/5
40/40
29/29
5/20
3/32
42/11
16/14
27/49
36/20
18/39
49/41
16/6
24/46
44/48
36/4
6/6
13/6
42/12
29/41
39/39
9/3
30/2
25/20
15/6
15/23
28/40
8/7
26/23
48/10
28/28
2/13
48/14
"""

def parse_components(lines):
    return [tuple(map(int, line.split("/"))) for line in lines]


def test_parse_components():
    expected = [(0,2),(2,2),(2,3),(3,4),(3,5),(0,1),(10,1),(9,10)]
    assert parse_components(TEST_INPUT.splitlines()) == expected


def bridges(components, sofar=()):
    last_port = sofar[-1][1] if sofar else 0
    for i, comp in enumerate(components):
        use_comp = None
        if comp[0] == last_port:
            use_comp = comp
        elif comp[1] == last_port:
            use_comp = comp[::-1]
        if use_comp:
            bridge = sofar + (use_comp,)
            yield bridge
            yield from bridges(components[:i] + components[i+1:], bridge)


def test_bridges():
    expected = {
        ((0,1),),
        ((0,1), (1,10),),
        ((0,1), (1,10), (10,9),),
        ((0,2),),
        ((0,2), (2,3),),
        ((0,2), (2,3), (3,4),),
        ((0,2), (2,3), (3,5),),
        ((0,2), (2,2),),
        ((0,2), (2,2), (2,3),),
        ((0,2), (2,2), (2,3), (3,4),),
        ((0,2), (2,2), (2,3), (3,5),),
    }
    components = parse_components(TEST_INPUT.splitlines())
    assert set(bridges(components)) == expected

def strength(bridge):
    return sum(sum(pair) for pair in bridge)


def best_bridge(components):
    return max(bridges(components), key=strength)

def test_best_bridge():
    components = parse_components(TEST_INPUT.splitlines())
    best = best_bridge(components)
    assert strength(best) == 31


if __name__ == '__main__':
    components = parse_components(INPUT.splitlines())
    best = best_bridge(components)
    print(f"Part 1: the strongest bridge has strength {strength(best)}")
