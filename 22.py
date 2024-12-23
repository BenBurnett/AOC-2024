import sys
from collections import defaultdict


def test_input_1():
    _input = """1
10
100
2024""".strip().split("\n")

    _input = [int(x) for x in _input]

    assert part_1(_input) == 37327623


def test_input_2():
    _input = """1
2
3
2024""".strip().split("\n")

    _input = [int(x) for x in _input]

    assert part_2(_input) == 23


def next_secret(secret, count=1):
    for _ in range(count):
        secret ^= (secret << 6) & 0xFFFFFF
        secret ^= (secret >> 5) & 0xFFFFFF
        secret ^= (secret << 11) & 0xFFFFFF
    return secret


def read_input(path: str):
    with open(path) as f:
        return [int(line.strip()) for line in f]


def part_1(input_data):
    return sum(next_secret(secret, 2000) for secret in input_data)


def part_2(input_data):
    count = 2000
    global_sequences = defaultdict(int)

    for secret in input_data:
        differences = []
        sequences = defaultdict(int)
        digit = secret % 10
        for _ in range(count):
            secret = next_secret(secret)
            new_digit = secret % 10
            differences.append(new_digit - digit)
            digit = new_digit
            sequence = tuple(differences[-4:])
            if len(sequence) < 4 or sequence in sequences:
                continue

            sequences[tuple(differences[-4:])] += new_digit

        for sequence, value in sequences.items():
            global_sequences[sequence] += value

    return max(global_sequences.values())


def main():
    input_data = read_input(sys.argv[1])
    print(f"Part 1: {part_1(input_data)}")

    print(f"Part 2: {part_2(input_data)}")


if __name__ == "__main__":
    main()
