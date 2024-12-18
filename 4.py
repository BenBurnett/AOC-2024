import sys


def test_input():
    _input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".strip().split("\n")

    assert part_1(_input) == 18
    assert part_2(_input) == 9


def read_input(path: str) -> list[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file.readlines()]


def part_1(input_data: list[str]) -> int:
    word = 'XMAS'
    word_len = len(word)
    imax = len(input_data)
    jmax = len(input_data[0])

    directions = [
        (0, 1),  # forwards
        (0, -1),  # backwards
        (1, 0),  # downwards
        (-1, 0),  # upwards
        (1, 1),  # diagonal down-right
        (-1, 1),  # diagonal up-right
        (1, -1),  # diagonal down-left
        (-1, -1)  # diagonal up-left
    ]

    def check_direction(i, j, di, dj):
        for k in range(word_len):
            ni, nj = i + k * di, j + k * dj
            if not (0 <= ni < imax and 0 <= nj < jmax) or input_data[ni][nj] != word[k]:
                return False
        return True

    def check_word(i, j):
        if input_data[i][j] != word[0]:
            return 0
        return sum(check_direction(i, j, di, dj) for di, dj in directions)

    return sum(check_word(i, j) for i in range(imax) for j in range(jmax))


def part_2(input_data: list[str]) -> int:
    imax = len(input_data) - 1
    jmax = len(input_data[0]) - 1

    directions = [
        ((-1, -1), (1, 1)),  # top left to bottom right
        ((1, -1), (-1, 1))  # bottom left to top right
    ]

    def check_word(i, j):
        if input_data[i][j] != 'A':
            return 0

        for dir in directions:
            if input_data[i + dir[0][0]][j + dir[0][1]] + input_data[i + dir[1][0]][j + dir[1][1]] not in ['MS', 'SM']:
                return 0

        return 1

    return sum(check_word(i, j) for i in range(1, imax) for j in range(1, jmax))


def main() -> None:
    input_data = read_input(sys.argv[1])
    print(f'Part 1: {part_1(input_data)}')
    print(f'Part 2: {part_2(input_data)}')


if __name__ == '__main__':
    main()
