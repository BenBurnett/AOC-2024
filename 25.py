import sys
from itertools import product


def test_input():
    _input = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####""".strip().split('\n')

    keys, locks = get_keys_and_locks(_input)
    assert part_1(keys, locks) == 3


def read_input(path: str):
    with open(path, 'r') as f:
        return [line.strip() for line in f]


def get_keys_and_locks(input_data):
    keys = []
    locks = []
    current = None
    is_key = False

    for line in input_data:
        if not line:
            if current is not None:
                (keys if is_key else locks).append(current)
                current = None
                continue

        if current is None:
            is_key = line[0] == '.'
            current = [-1] * 5
        current = [sum(x) for x in zip(current, [1 if c == '#' else 0 for c in line])]

    if current is not None:
        (keys if is_key else locks).append(current)

    return keys, locks


def part_1(keys, locks):
    return sum(1 for lock, key in product(locks, keys) if all(l + k <= 5 for l, k in zip(lock, key)))


def main():
    input_data = read_input(sys.argv[1])
    keys, locks = get_keys_and_locks(input_data)

    print(f'Part 1: {part_1(keys, locks)}')


if __name__ == '__main__':
    main()
