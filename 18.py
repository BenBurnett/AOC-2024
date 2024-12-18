import bisect
import sys
from heapq import heappop, heappush

DIRECTIONS = [
    (1, 0),  # right
    (0, 1),  # down
    (-1, 0),  # left
    (0, -1),  # up
]


class DijkstraGraph():

    def __init__(self, falling_bytes: list[tuple[int, int]], end: int):
        self.falling_bytes = falling_bytes
        self.end = end
        self.direction = 0

    def move(self, position: tuple[int, int], direction: int) -> tuple[int, int]:
        x, y = position
        dx, dy = DIRECTIONS[direction]
        return (x + dx, y + dy)

    def solve(self) -> int:
        visited = {}

        queue = [(0, (0, 0), self.direction)]

        while queue:
            score, position, direction = heappop(queue)
            px, py = position

            if position == (self.end, self.end):
                return score

            if px < 0 or px > self.end or py < 0 or py > self.end:
                continue

            if position in self.falling_bytes:
                continue

            if (position, direction) in visited and visited[(position, direction)] <= score:
                continue
            visited[(position, direction)] = score

            for new_direction in [direction, (direction - 1) % 4, (direction + 1) % 4]:
                heappush(queue, (score + 1, self.move(position, new_direction), new_direction))

        return 0


def test_input():
    _input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip().split("\n")

    assert part_1(_input, 12, 6) == 22
    assert part_2(_input, 6) == '6,1'


def read_input(path: str) -> list[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def get_coordinates(input_data: list[str]) -> list[tuple[int, int]]:
    return [tuple(map(int, line.split(','))) for line in input_data]


def part_1(input_data: list[str], num_coords: int, max: int) -> int:
    graph = DijkstraGraph(get_coordinates(input_data)[:num_coords], max)
    return graph.solve()


def part_2(input_data: list[str], max: int) -> str:
    coordinates = get_coordinates(input_data)
    index = bisect.bisect_left(range(len(coordinates)),
                               True,
                               key=lambda x: DijkstraGraph(coordinates[:x + 1], max).solve() == 0)
    return f'{coordinates[index][0]},{coordinates[index][1]}'


def main() -> None:
    input_data = read_input(sys.argv[1])
    print(f'Part 1: {part_1(input_data, 1024, 70)}')
    print(f'Part 2: {part_2(input_data, 70)}')


if __name__ == '__main__':
    main()
