import sys


def test_input():
    _input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip().split("\n")

    reports = get_reports(_input)
    assert part_1(reports) == 2
    assert part_2(reports) == 4


def read_input(path: str) -> list[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def get_reports(input_data: list[str]) -> list[list[int]]:
    return [list(map(int, line.split())) for line in input_data]


def is_valid_report(report):
    vals = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return (all(v > 0 for v in vals) or all(v < 0 for v in vals)) and all(abs(v) <= 3 for v in vals)


def is_valid_report_with_level_removed(report):
    if is_valid_report(report):
        return True
    return any(is_valid_report(report[:i] + report[i + 1:]) for i in range(len(report)))


def part_1(reports: list[list[int]]) -> int:
    return sum(1 for report in reports if is_valid_report(report))


def part_2(reports: list[list[int]]) -> int:
    return sum(1 for report in reports if is_valid_report_with_level_removed(report))


def main() -> None:
    input_data = read_input(sys.argv[1])
    reports = get_reports(input_data)
    print(f'Part 1: {part_1(reports)}')
    print(f'Part 2: {part_2(reports)}')


if __name__ == '__main__':
    main()
