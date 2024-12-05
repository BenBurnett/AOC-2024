from collections import Counter
from itertools import takewhile

with open('input.txt') as f:
    lines = [line.strip() for line in f]

rules = set(takewhile(lambda x: x != '', lines))
updates = [line.split(',') for line in lines[len(rules) + 1:]]


def check_update(update):
    update_rules = [rule for rule in rules if all(part in update for part in rule.split('|'))]
    update_counter = Counter([rule.split('|')[0] for rule in update_rules])

    if [x[0] for x in update_counter.most_common()] == update[:-1]:
        return 0

    return int(update_counter.most_common()[len(update) // 2][0])


total = sum(check_update(update) for update in updates)
print(total)
