from collections import deque


class Trail:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def score(self):
        seen = set()
        queue = deque()
        queue.append((
            0,
            self.x,
            self.y,
        ))

        while queue:
            val, x, y = queue.popleft()

            if x < 0 or y < 0 or x >= xmax or y >= ymax:
                continue

            if int(lines[y][x]) != val:
                continue

            if val == 9:
                seen.add((x, y))
                continue

            queue.append((val + 1, x + 1, y))
            queue.append((val + 1, x - 1, y))
            queue.append((val + 1, x, y + 1))
            queue.append((val + 1, x, y - 1))

        return len(seen)


with open('input.txt') as f:
    lines = [line.strip() for line in f]

xmax = len(lines[0])
ymax = len(lines)

score = 0
for yi in range(ymax):
    for xi in range(xmax):
        if lines[yi][xi] == '0':
            score += Trail(xi, yi).score()

print(score)
