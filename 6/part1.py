import bisect
from collections import defaultdict

xdict = defaultdict(list)
ydict = defaultdict(list)

pos = (0, 0)
with open('input.txt') as f:
    lines = [line.strip() for line in f]

for yi, line in enumerate(lines):
    for xi, letter in enumerate(line):
        if letter == '#':
            xdict[xi].append(yi)
            ydict[yi].append(xi)
        elif letter == '^':
            pos = (xi, yi)

dicts = [xdict, ydict]

directions = [
    (0, -1),  # up
    (1, 1),  # right
    (0, 1),  # down
    (1, -1)  # left
]
direction = 0


def get_next_pos(pos, direction):
    dx, dy = directions[direction]
    d = dicts[dx]
    delta = -1 if dy == -1 else 0

    idx = bisect.bisect_left(d[pos[dx]], pos[1 - dx]) + delta
    if idx < 0 or idx >= len(d[pos[dx]]):
        raise IndexError

    new_pos = (pos[0], d[pos[0]][idx] - dy) if dx == 0 else (d[pos[1]][idx] - dy, pos[1])
    return new_pos


positions = [pos]
while True:
    try:
        pos = get_next_pos(pos, direction)
    except IndexError:
        px, py = pos
        dx, dy = directions[direction]
        if dx == 0:
            positions.append((px, 0 if dy == -1 else len(lines) - 1))
        else:
            positions.append((0 if dx == -1 else len(lines[0]) - 1, py))
        break

    positions.append(pos)
    direction = (direction + 1) % 4


def get_inner_positions(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    else:
        return [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]


stuff = set()
for i in range(len(positions) - 1):
    stuff.update(get_inner_positions(positions[i], positions[i + 1]))

print(len(stuff))
