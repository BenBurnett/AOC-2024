with open('input.txt') as f:
    lines = [line.strip() for line in f]

imax = len(lines) - 1
jmax = len(lines[0]) - 1

directions = [
    ((-1, -1), (1, 1)),  # top left to bottom right
    ((1, -1), (-1, 1))  # bottom left to top right
]


def check_word(i, j):
    if lines[i][j] != 'A':
        return 0

    for dir in directions:
        if lines[i + dir[0][0]][j + dir[0][1]] + lines[i + dir[1][0]][j + dir[1][1]] not in ['MS', 'SM']:
            return 0

    return 1


count = sum(check_word(i, j) for i in range(1, imax) for j in range(1, jmax))

print(count)
