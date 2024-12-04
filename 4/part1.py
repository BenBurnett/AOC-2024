with open('input.txt') as f:
    lines = [line.strip() for line in f]

word = 'XMAS'
word_len = len(word)
imax = len(lines)
jmax = len(lines[0])

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
        if not (0 <= ni < imax and 0 <= nj < jmax) or lines[ni][nj] != word[k]:
            return False
    return True


def check_word(i, j):
    if lines[i][j] != word[0]:
        return 0
    return sum(check_direction(i, j, di, dj) for di, dj in directions)


count = sum(check_word(i, j) for i in range(imax) for j in range(jmax))

print(count)
