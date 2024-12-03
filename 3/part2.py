import re

exp = r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))'

with open('input.txt') as f:
    code = f.read().strip()

do = True


def solve_match(match):
    global do

    if "mul" in match[0] and do:
        return int(match[1]) * int(match[2])

    do = True if "do()" in match[0] else False

    return 0


matches = re.findall(exp, code)
result = sum(solve_match(match) for match in matches)

print(result)
