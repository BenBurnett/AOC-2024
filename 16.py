import sys
from heapq import heappop, heappush

DIRECTIONS = [
    (1, 0),  # right
    (0, 1),  # down
    (-1, 0),  # left
    (0, -1),  # up
]


class DijkstraGraph():

    def __init__(self, input_data: list[str], start: tuple[int, int], end: tuple[int, int]):
        self.input_data = input_data
        self.start = start
        self.end = end
        self.direction = 0

    def move(self, position: tuple[int, int], direction: int) -> tuple[int, int]:
        x, y = position
        dx, dy = DIRECTIONS[direction]

        return (x + dx, y + dy)

    def solve(self) -> tuple[int, int]:
        visited = {}
        min_score = None
        full_path = set()

        queue = [(0, self.start, self.direction, [])]

        while queue:
            score, position, direction, path = heappop(queue)
            path.append(position)

            if position == self.end:
                if min_score is None or score == min_score:
                    min_score = score
                    full_path.update(path)
                continue

            if self.input_data[position[1]][position[0]] == '#':
                continue

            if (position, direction) in visited and visited[(position, direction)] < score:
                continue
            visited[(position, direction)] = score

            for new_direction in [direction, (direction - 1) % 4, (direction + 1) % 4]:
                new_position = self.move(position, new_direction)
                new_score = score + 1 if new_direction == direction else score + 1001
                heappush(queue, (new_score, new_position, new_direction, path.copy()))

        return min_score, len(full_path)


def test_input_1():
    _input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".split("\n")

    assert DijkstraGraph(_input, *get_start_end(_input)).solve() == (7036, 45)


def test_input_2():
    _input = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################""".split("\n")

    assert DijkstraGraph(_input, *get_start_end(_input)).solve() == (11048, 64)


def read_input(path: str) -> list[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def get_start_end(input_data: list[str]) -> tuple[tuple[int, int], tuple[int, int]]:
    start = (1, len(input_data) - 2)
    end = (len(input_data[0]) - 2, 1)
    return start, end


def main() -> None:
    input_data = read_input(sys.argv[1])
    graph = DijkstraGraph(input_data, *get_start_end(input_data))
    part1, part2 = graph.solve()
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == '__main__':
    main()
