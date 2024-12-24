import re
import sys
from fractions import Fraction


def test_input() -> None:
    _input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".strip().split("\n")

    equations = get_equations(_input)

    assert part_1(equations) == 480
    assert part_2(equations) == 875318608908


def read_input(path: str) -> list[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def get_equations(input_data: list[str]) -> list[list[list[int]]]:
    equations = []
    a = b = constants = None

    for line in input_data:
        if "Button A" in line:
            a = list(map(int, re.findall(r"[-+]?\d+", line)))
        elif "Button B" in line:
            b = list(map(int, re.findall(r"[-+]?\d+", line)))
        elif "Prize" in line:
            constants = list(map(int, re.findall(r"[-+]?\d+", line)))
            if a and b:
                equations.append([[a[0], b[0], constants[0]], [a[1], b[1], constants[1]]])
            a = b = constants = None

    return equations


def solve_linear_equations(equations: list[list[list[int]]]) -> tuple[Fraction, Fraction]:
    a, b, c = equations[0]
    d, e, f = equations[1]

    factor = Fraction(d, a)
    d -= factor * a
    e -= factor * b
    f -= factor * c

    y = Fraction(f, e)
    x = Fraction(c - b * y, a)

    return x, y


def part_1(equations: list[list[list[int]]]) -> list[tuple[Fraction, Fraction]]:
    return sum(
        int(solution[0]) * 3 + int(solution[1])
        for eq in equations
        if all(map(lambda x: x.denominator == 1, (solution := solve_linear_equations(eq)))))


def part_2(equations: list[list[list[int]]]) -> int:
    OFFSET = 10000000000000
    total = 0
    for eq in equations:
        modified_eq = [[eq[0][0], eq[0][1], eq[0][2] + OFFSET], [eq[1][0], eq[1][1], eq[1][2] + OFFSET]]
        solution = solve_linear_equations(modified_eq)
        if all(x.denominator == 1 for x in solution):
            total += int(solution[0]) * 3 + int(solution[1])
    return total


def main() -> None:
    input_data = read_input(sys.argv[1])
    equations = get_equations(input_data)

    print(f'Part 1: {part_1(equations)}')
    print(f'Part 2: {part_2(equations)}')


if __name__ == "__main__":
    main()
