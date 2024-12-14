from collections import deque

with open('input.txt') as f:
    data = f.read().splitlines()

xmax = len(data[0])
ymax = len(data)

total_seen = set()


def count_corners(plant, x, y):
    up = data[y - 1][x] if y - 1 >= 0 else None
    down = data[y + 1][x] if y + 1 < ymax else None
    left = data[y][x - 1] if x - 1 >= 0 else None
    right = data[y][x + 1] if x + 1 < xmax else None

    count = sum(1 for i in (up, down, left, right) if i == plant)

    corners = 0

    if count == 0:
        return 4
    if count == 1:
        return 2
    if count == 2:
        if left == right == plant or up == down == plant:
            return 0
        corners += 1

    if up == left == plant and (y - 1 >= 0 and x - 1 >= 0) and data[y - 1][x - 1] != plant:
        corners += 1
    if up == right == plant and (y - 1 >= 0 and x + 1 < xmax) and data[y - 1][x + 1] != plant:
        corners += 1
    if down == left == plant and (y + 1 < ymax and x - 1 >= 0) and data[y + 1][x - 1] != plant:
        corners += 1
    if down == right == plant and (y + 1 < ymax and x + 1 < xmax) and data[y + 1][x + 1] != plant:
        corners += 1

    return corners


def calc_plot(x, y):
    plant = data[y][x]

    perimeter = 0
    area = 0
    corners = 0
    seen = set()

    q = deque()
    q.append((x, y))

    while q:
        xi, yi = q.popleft()

        if (xi, yi) in seen:
            continue

        if xi < 0 or xi >= xmax or yi < 0 or yi >= ymax or data[yi][xi] != plant:
            perimeter += 1
            continue

        seen.add((xi, yi))
        area += 1
        corners += count_corners(plant, xi, yi)

        q.append((xi + 1, yi))
        q.append((xi - 1, yi))
        q.append((xi, yi + 1))
        q.append((xi, yi - 1))

    total_seen.update(seen)

    return area * corners


total = 0
for yi in range(ymax):
    for xi in range(xmax):
        if (xi, yi) in total_seen:
            continue

        total += calc_plot(xi, yi)

print(total)
