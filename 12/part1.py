from collections import deque

with open('input.txt') as f:
    data = f.read().splitlines()

xmax = len(data[0])
ymax = len(data)

total_seen = set()


def calc_plot(x, y):
    plant = data[y][x]

    perimeter = 0
    area = 0
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

        q.append((xi + 1, yi))
        q.append((xi - 1, yi))
        q.append((xi, yi + 1))
        q.append((xi, yi - 1))

    total_seen.update(seen)
    return area * perimeter


total = 0
for yi in range(ymax):
    for xi in range(xmax):
        if (xi, yi) in total_seen:
            continue

        total += calc_plot(xi, yi)

print(total)
