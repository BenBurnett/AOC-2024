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

    a1 = (x2 + dx, y2 + dy)
    a2 = (x1 - dx, y1 - dy)

    return [a for a in [a1, a2] if is_valid_antinode(*a)]


antinodes = set()
for v in nodes.values():
    for combo in itertools.combinations(v, 2):
        antinodes.update(calculate_antinodes(combo[0], combo[1]))

print(len(antinodes))
