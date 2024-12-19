import sys
from functools import cache


def test_input():
    _input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".strip().split("\n")

    towels, patterns = get_towels_and_patterns(_input)
    assert part_1(towels, patterns) == 6
    assert part_2(towels, patterns) == 16


def read_input(path: str) -> list[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file.readlines()]


def get_towels_and_patterns(input_data: list[str]) -> tuple[list[str], list[str]]:
    towels = [t.strip() for t in input_data[0].strip().split(',')]
    patterns = [line for line in input_data[1:] if line]
    return towels, patterns


def solve(towels: list[str], pattern: str) -> int:

    @cache
    def _solve(pattern: str) -> int:
        if not pattern:
            return 1
        return sum(_solve(pattern[len(towel):]) for towel in towels if pattern.startswith(towel))

    return _solve(pattern)


def part_1(towels: list[str], patterns: list[str]) -> int:
    return sum(1 if solve(towels, pattern) else 0 for pattern in patterns)


def part_2(towels: list[str], patterns: list[str]) -> int:
    return sum(solve(towels, pattern) for pattern in patterns)


def main() -> None:
    input_data = read_input(sys.argv[1])
    towels, patterns = get_towels_and_patterns(input_data)
    print(f'Part 1: {part_1(towels, patterns)}')
    print(f'Part 2: {part_2(towels, patterns)}')


if __name__ == '__main__':
    main()
