import re
import sys


def test_input_1():
    _input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
    assert part_1(_input) == 161


def test_input_2():
    _input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
    assert part_2(_input) == 48


def read_input(path: str) -> str:
    with open(path) as input_file:
        return input_file.read().strip()


def part_1(code: str) -> int:
    exp = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    return sum(int(match[0]) * int(match[1]) for match in exp.findall(code))


def part_2(code: str) -> int:
    exp = re.compile(r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))')

    do = True
    total = 0

    for match in exp.findall(code):
        if match[0].startswith("mul") and do:
            total += int(match[1]) * int(match[2])
        elif match[0].startswith("do()"):
            do = True
        elif match[0].startswith("don't()"):
            do = False

    return total


def main() -> None:
    code = read_input(sys.argv[1])
    print(f'Part 1: {part_1(code)}')
    print(f'Part 2: {part_2(code)}')


if __name__ == '__main__':
    main()
