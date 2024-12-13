import itertools
from collections import defaultdict

nodes = defaultdict(set)

with open('input.txt') as f:
    lines = [line.strip() for line in f]

for yi, line in enumerate(lines):
    for xi, char in enumerate(line):
        if char != '.':
            nodes[char].add((xi, yi))

xmax = len(lines[0])
ymax = len(lines)


def is_valid_antinode(x, y):
    return 0 <= x < xmax and 0 <= y < ymax


def calculate_antinodes(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    antinodes = {p1, p2}

    a1 = (x2 + dx, y2 + dy)
    while is_valid_antinode(*a1):
        antinodes.add(a1)
        a1 = (a1[0] + dx, a1[1] + dy)

    a2 = (x1 - dx, y1 - dy)
    while is_valid_antinode(*a2):
        antinodes.add(a2)
        a2 = (a2[0] - dx, a2[1] - dy)

    return antinodes


antinodes = set()
for v in nodes.values():
    for combo in itertools.combinations(v, 2):
        antinodes.update(calculate_antinodes(combo[0], combo[1]))

print(len(antinodes))
