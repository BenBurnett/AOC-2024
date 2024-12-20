import sys
from collections import deque
from typing import Generator


def test_input():
    _input = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".strip().split("\n")

    start = get_start(_input)
    graph = Pathfinder(_input, start)
    path = graph.solve()

    assert get_cheats(path, 2, 1) == 44
    assert get_cheats(path, 20, 50) == 285


DIRECTIONS = [
    (1, 0),  # right
    (0, 1),  # down
    (-1, 0),  # left
    (0, -1),  # up
]


class Pathfinder():

    def __init__(self, grid: list[str], start: tuple[int, int]):
        self.grid = grid
        self.start = start
        self.direction = 0

        for i, _ in enumerate(DIRECTIONS):
            pos = self.move(self.start, i)
            if self.grid[pos[1]][pos[0]] == '.':
                self.direction = i
                break

    def move(self, position: tuple[int, int], direction: int) -> tuple[int, int]:
        x, y = position
        dx, dy = DIRECTIONS[direction]
        return (x + dx, y + dy)

    def solve(self) -> list[tuple[int, int]]:
        queue = deque([(self.start, self.direction)])
        path = []

        while queue:
            position, direction = queue.popleft()
            path.append(position)

            for new_direction in [direction, (direction - 1) % 4, (direction + 1) % 4]:
                new_position = self.move(position, new_direction)
                if self.grid[new_position[1]][new_position[0]] in 'E.':
                    queue.append((new_position, new_direction))
                    break

        return path


def read_input(path: str) -> list[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def get_start(input_data: list[str]) -> tuple[int, int]:
    for yi, line in enumerate(input_data):
        if 'S' in line:
            return (line.index('S'), yi)
    raise ValueError('Start not found')


def get_cheats(path: list[tuple[int, int]], cheat_len: int = 2, cheat_score: int = 1) -> int:
    point_index = {point: i for i, point in enumerate(path)}
    cheats = 0

    visited = set()

    for point in path:
        for distance in range(cheat_len, 1, -1):
            for new_point in manhattan_ring(point, distance):
                if new_point in visited or new_point not in point_index:
                    continue

                if point_index[new_point] - point_index[point] - distance < cheat_score:
                    visited.add(new_point)
                    continue

                cheats += 1

    return cheats


def manhattan_ring(point: tuple[int, int], distance: int) -> Generator[tuple[int, int], None, None]:
    x, y = point
    for i in range(distance):
        yield x + distance - i, y + i
        yield x - i, y + distance - i
        yield x - distance + i, y - i
        yield x + i, y - distance + i


def main() -> None:
    input_data = read_input(sys.argv[1])
    start = get_start(input_data)
    graph = Pathfinder(input_data, start)
    path = graph.solve()

    print(f'Part 1: {get_cheats(path, 2, 100)}')
    print(f'Part 2: {get_cheats(path, 20, 100)}')


if __name__ == '__main__':
    main()
