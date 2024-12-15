from collections import Counter
import re
from xmlrpc.client import MAXINT

width = 101  #11
half_width = width // 2
height = 103  #7
half_height = height // 2


class Robot:

    def __init__(self, px, py, vx, vy) -> None:
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.q = None

    def move(self, seconds):
        self.px = (self.px + self.vx * seconds) % width
        self.py = (self.py + self.vy * seconds) % height
        self.q = self.quadrant()

    def quadrant(self):
        quadrants = {
            (True, True): 1,
            (True, False): 3,
            (False, True): 2,
            (False, False): 4,
        }
        return quadrants[(self.px < half_width,
                          self.py < half_height)] if self.px != half_width and self.py != half_height else None


with open('input.txt') as f:
    robots = [Robot(*map(int, re.findall(r'(-?\d+)', line))) for line in f]


def print_grid(robots: list[Robot]):
    grid = [list('.' * width) for _ in range(height)]

    for robot in robots:
        val = grid[robot.py][robot.px]
        grid[robot.py][robot.px] = '1' if val == '.' else str(int(val) + 1)

    print('\n'.join(''.join(row) for row in grid))


count = 0
safety_min = MAXINT

while True:
    count += 1
    quadrants = []
    for robot in robots:
        robot.move(1)
        quadrants.append(robot.q)

    counter = Counter(quadrants)
    counter.pop(None)
    safety_score = counter[1] * counter[2] * counter[3] * counter[4]

    if safety_score < safety_min:
        safety_min = safety_score
        print_grid(robots)
        print(f'New safety score: {safety_score} at {count} seconds')
