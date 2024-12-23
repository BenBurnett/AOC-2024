import sys
from collections import Counter
from functools import cache


def test_input():
    _input = """029A
980A
179A
456A
379A""".strip().split('\n')

    assert part_1(_input) == 126384


class Pad:
    LOOKUPS = {}

    def inputs(self, sequence: str):
        inputs = []

        def _inputs(result, current, sequence):
            if len(sequence) == 0:
                inputs.append(result)
                return
            for move in self._inputs(current, sequence[0]):
                _inputs(result + move, sequence[0], sequence[1:])

        _inputs('', 'A', sequence)

        return inputs

    def _inputs(self, start: str, end: str):
        sx, sy = self.LOOKUPS[start]
        ex, ey = self.LOOKUPS[end]
        dx, dy = ex - sx, ey - sy

        x_str = '<' * -dx if dx < 0 else '>' * dx
        y_str = '^' * -dy if dy < 0 else 'v' * dy

        value = []
        if dy != 0 and (sx, sy + dy) != self.LOOKUPS[' ']:
            value.append(f'{y_str}{x_str}A')
        if dx != 0 and (sx + dx, sy) != self.LOOKUPS[' ']:
            value.append(f'{x_str}{y_str}A')
        if dx == dy == 0:
            value.append('A')

        return value


class Numpad(Pad):
    """
    A class representing a numpad with a specific layout.

    The numpad layout is as follows:
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+

    Attributes:
        LOOKUPS (dict): A dictionary containing lookup values for the numpad.
    """

    LOOKUPS = {
        '7': (0, 0),
        '8': (1, 0),
        '9': (2, 0),
        '4': (0, 1),
        '5': (1, 1),
        '6': (2, 1),
        '1': (0, 2),
        '2': (1, 2),
        '3': (2, 2),
        ' ': (0, 3),
        '0': (1, 3),
        'A': (2, 3),
    }


class Dirpad(Pad):
    """
    A class representing a direction pad with a specific layout.
    
    The direction pad layout is as follows:
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+

    Attributes:
        LOOKUPS (dict): A dictionary containing lookup values for the direction pad.
    """

    LOOKUPS = {
        ' ': (0, 0),
        '^': (1, 0),
        'A': (2, 0),
        '<': (0, 1),
        'v': (1, 1),
        '>': (2, 1),
    }


def read_input(path: str) -> list[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file]


@cache
def shortest(sequence: str, depth: int):
    dirpad = Dirpad()
    if depth == 0:
        return len(sequence)

    total = 0
    for sub in sequence.split('A')[:-1]:
        sequences = dirpad.inputs(sub + 'A')
        total += min(shortest(seq, depth - 1) for seq in sequences)
    return total


def score_at_depth(input_data: list[str], depth: int) -> int:
    total = 0
    numpad = Numpad()
    for code in input_data:
        numcode = numpad.inputs(code)
        min_len = min(shortest(nc, depth) for nc in numcode)
        total += min_len * int(code[:-1])
    return total


def part_1(input_data: list[str]) -> int:
    return score_at_depth(input_data, 2)


def part_2(input_data: list[str]) -> int:
    return score_at_depth(input_data, 25)


def main():
    input_data = read_input(sys.argv[1])
    print(f'Part 1: {part_1(input_data)}')
    print(f'Part 2: {part_2(input_data)}')


if __name__ == '__main__':
    main()
