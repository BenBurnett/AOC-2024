import re

exp = r'mul\((\d{1,3}),(\d{1,3})\)'

with open('input.txt') as f:
    code = f.read().strip()


def solve_match(match):
    return int(match[0]) * int(match[1])


result = sum(solve_match(match) for match in re.findall(exp, code))

print(result)
