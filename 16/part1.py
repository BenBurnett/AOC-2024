import heapq
from typing import Set, Tuple

with open('input.txt') as f:
    lines = f.read().splitlines()

start = (1, len(lines) - 2)
start_direction = 1  # right
start_tuple = (*start, start_direction)
visited: Set[Tuple[int, int, int]] = set()
visited.add(start_tuple)

DIRECTIONS = [
    (0, -1),  # up
    (1, 0),  # right
    (0, 1),  # down
    (-1, 0)  # left
]


class Status:
    ACTIVE = 0
    DONE = 1
    FAILED = 2


class Path:

    def __init__(self, position, direction, score=0):
        self.x, self.y = position
        self.direction = direction
        self.score = score
        self.status = Status.ACTIVE

    def __lt__(self, other):
        return self.score < other.score

    def move(self):
        dx, dy = DIRECTIONS[self.direction]
        new_x, new_y = self.x + dx, self.y + dy
        if (new_x, new_y, self.direction) in visited or lines[new_y][new_x] == '#':
            self.status = Status.FAILED
        else:
            self.x, self.y = new_x, new_y
            self.score += 1
            if lines[new_y][new_x] == 'E':
                self.status = Status.DONE
            visited.add((new_x, new_y, self.direction))


paths = []
queue = []
path = Path(start, start_direction)
heapq.heappush(queue, (path.score, path))

while queue:
    _, p = heapq.heappop(queue)

    if p.status == Status.DONE:
        paths.append(p)
        continue
    elif p.status == Status.FAILED:
        continue

    for turn in [1, -1]:
        new_direction = (p.direction + turn) % 4
        new_path = Path((p.x, p.y), new_direction, p.score + 1000)
        new_path.move()
        if new_path.status != Status.FAILED:
            heapq.heappush(queue, (new_path.score, new_path))

    p.move()
    if p.status != Status.FAILED:
        heapq.heappush(queue, (p.score, p))

print(min(p.score for p in paths if p.status == Status.DONE))
