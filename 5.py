import sys
from collections import Counter
from itertools import takewhile


def test_input():
    _input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".strip().split("\n")

    rules, updates = get_rules_and_updates(_input)
    assert part_1(rules, updates) == 143
    assert part_2(rules, updates) == 123


def read_input(path: str) -> list[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file.readlines()]


def get_rules_and_updates(input_data: list[str]) -> tuple[set[str], list[list[str]]]:
    rules = set(takewhile(bool, input_data))
    updates = [line.split(',') for line in input_data[len(rules) + 1:]]

    return rules, updates


def part_1(rules, updates) -> int:
    return sum(check_update(update, rules, True) for update in updates)


def part_2(rules, updates) -> int:
    return sum(check_update(update, rules, False) for update in updates)


def check_update(update: list[str], rules: set[str], sorted: bool) -> int:
    update_rules = [rule for rule in rules if all(part in update for part in rule.split('|'))]
    update_counter = Counter(rule.split('|')[0] for rule in update_rules)

    most_common = [x[0] for x in update_counter.most_common()]
    if (sorted and most_common != update[:-1]) or (not sorted and most_common == update[:-1]):
        return 0

    return int(update_counter.most_common()[len(update) // 2][0])


def main() -> None:
    input_data = read_input(sys.argv[1])
    rules, updates = get_rules_and_updates(input_data)
    print(f'Part 1: {part_1(rules, updates)}')
    print(f'Part 2: {part_2(rules, updates)}')


if __name__ == '__main__':
    main()
