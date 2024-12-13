import itertools

found = 0
with open('input.txt') as f:
    for line in f:
        answer, parts = line.strip().split(':')
        parts = parts.strip().split(' ')

        for operators in itertools.product('+*', repeat=len(parts) - 1):
            total = int(parts[0])
            for i in range(1, len(parts)):
                if operators[i - 1] == '+':
                    total += int(parts[i])
                else:
                    total *= int(parts[i])

            if total == int(answer):
                found += total
                break

print(found)
