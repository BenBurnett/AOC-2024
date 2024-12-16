import heapq
from typing import Set, Tuple

with open('input.txt') as f:
    lines = f.read().splitlines()

start = (1, len(lines) - 2)
start_direction = 1  # right
start_tuple = (*start, start_direction)

visited = {start_tuple: 0}

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
        self.sequence = [position]

    def __lt__(self, other):
        return self.score < other.score

    def move(self):
        dx, dy = DIRECTIONS[self.direction]
        new_x, new_y = self.x + dx, self.y + dy

        if lines[new_y][new_x] == 'E':
            self.status = Status.DONE
            self.sequence.append((new_x, new_y))
            return
        elif lines[new_y][new_x] == '#' or ((new_x, new_y, self.direction) in visited and
                                            visited[(new_x, new_y, self.direction)] < self.score):
            self.status = Status.FAILED
            return

        self.x, self.y = new_x, new_y
        self.score += 1
        self.sequence.append((new_x, new_y))

        visited[(new_x, new_y, self.direction)] = self.score


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
        new_path.sequence = p.sequence.copy()
        new_path.move()
        if new_path.status != Status.FAILED:
            heapq.heappush(queue, (new_path.score, new_path))

    p.move()
    if p.status != Status.FAILED:
        heapq.heappush(queue, (p.score, p))


def print_grid():
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if (x, y) in unique_nodes:
                print('O', end='')
            else:
                print(char if char != '.' else ' ', end='')
        print()


min_score = min(p.score for p in paths if p.status == Status.DONE)
print(min_score)

min_score_paths = [p.sequence for p in paths if p.status == Status.DONE and p.score == min_score]
unique_nodes = set(node for path in min_score_paths for node in path)

print_grid()
print(len(unique_nodes))
