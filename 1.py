import sys
from collections import Counter


def test_input():
    _input = """3   4
4   3
2   5
1   3
3   9
3   3""".strip().split("\n")

    left, right = get_lists(_input)
    assert part_1(left, right) == 11
    assert part_2(left, right) == 31


def read_input(path: str) -> list[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def part_1(left: list[int], right: list[int]) -> int:
    return sum(abs(x - y) for x, y in zip(sorted(left), sorted(right)))


def part_2(left: list[int], right: list[int]) -> int:
    return sum(k * Counter(left).get(k, 0) * v for k, v in Counter(right).items())


def get_lists(input_data: list[str]) -> tuple[list[int], list[int]]:
    list1, list2 = zip(*(map(int, line.split()) for line in input_data))
    return list(list1), list(list2)


def main() -> None:
    input_data = read_input(sys.argv[1])
    left, right = get_lists(input_data)
    print(f'Part 1: {part_1(left, right)}')
    print(f'Part 2: {part_2(left, right)}')


if __name__ == '__main__':
    main()
