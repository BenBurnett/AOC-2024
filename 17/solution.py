import re
import sys


class Computer:

    def __init__(self, registers: dict[str, int], program: list[int]):
        self.registers = registers
        self.program = program
        self.pointer = 0
        self.output = []

    def run(self) -> None:
        while self.pointer < len(self.program) - 1:
            instruction = self.program[self.pointer]
            operand = self.program[self.pointer + 1]
            self.pointer += 2

            combo_operand = {
                4: self.registers['A'],
                5: self.registers['B'],
                6: self.registers['C'],
            }.get(operand, operand)

            match instruction:
                case 0:  # adv
                    self.registers['A'] //= 2**combo_operand
                case 1:  # bxl
                    self.registers['B'] ^= operand
                case 2:  # bst
                    self.registers['B'] = combo_operand % 8
                case 3:  # jnz
                    if self.registers['A'] != 0:
                        self.pointer = operand
                case 4:  # bxc
                    self.registers['B'] ^= self.registers['C']
                case 5:  # out
                    self.output.append(combo_operand % 8)
                case 6:  # bdv
                    self.registers['B'] = self.registers['A'] // (2**combo_operand)
                case 7:  # cdv
                    self.registers['C'] = self.registers['A'] // (2**combo_operand)


def test_1():
    computer = Computer({'A': 0, 'B': 0, 'C': 9}, [2, 6])
    computer.run()
    assert computer.registers['B'] == 1


def test_2():
    computer = Computer({'A': 10, 'B': 0, 'C': 0}, [5, 0, 5, 1, 5, 4])
    computer.run()
    assert computer.output == [0, 1, 2]


def test_3():
    computer = Computer({'A': 2024, 'B': 0, 'C': 0}, [0, 1, 5, 4, 3, 0])
    computer.run()
    assert computer.registers['A'] == 0
    assert computer.output == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]


def test_4():
    computer = Computer({'A': 0, 'B': 29, 'C': 0}, [1, 7])
    computer.run()
    assert computer.registers['B'] == 26


def test_5():
    computer = Computer({'A': 0, 'B': 2024, 'C': 43690}, [4, 0])
    computer.run()
    assert computer.registers['B'] == 44354


def test_6():
    computer = Computer({'A': 729, 'B': 0, 'C': 0}, [0, 1, 5, 4, 3, 0])
    computer.run()
    assert computer.output == [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]


def test_7():
    registers, program = {'A': 2024, 'B': 0, 'C': 0}, [0, 3, 5, 4, 3, 0]
    possible = solve_for_a(0, len(program) - 1, registers, program)
    assert min(possible) == 117440


def read_input(path: str) -> list[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def get_registers_and_program(input_data: list[str]) -> tuple[dict[str, int], list[int]]:
    registers = {}
    program = []
    for line in input_data:
        if match := re.match(r"Register (\w): (\d+)", line):
            registers[match.group(1)] = int(match.group(2))
        elif line.startswith("Program:"):
            program = list(map(int, line.split(":")[1].split(",")))
    return registers, program


def solve_for_a(a, idx, registers: dict[str, int], program: list[int]) -> list[int]:
    results = []

    for _ in range(8):
        registers['A'] = a
        computer = Computer(registers, program)
        computer.run()

        if computer.output[idx:] == program[idx:]:
            if idx == 0:
                results.append(a)
            else:
                results.extend(solve_for_a(a, idx - 1, registers, program))

        a += 0o1 << idx * 3

    return results


def part_1(registers: dict[str, int], program: list[int]) -> None:
    computer = Computer(registers, program)
    computer.run()
    print(f'Part 1: {",".join(str(c) for c in computer.output)}')


def part_2(registers: dict[str, int], program: list[int]) -> None:
    possible = solve_for_a(0, len(program) - 1, registers, program)
    print(f'Part 2: {min(possible)}')


def main() -> None:
    input_data = read_input(sys.argv[1])
    registers, program = get_registers_and_program(input_data)

    part_1(registers, program)
    part_2(registers, program)


if __name__ == '__main__':
    main()
