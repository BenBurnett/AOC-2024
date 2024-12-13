import itertools

found = 0
with open('input.txt') as f:
    for line in f:
        answer, parts = line.strip().split(':')
        parts = parts.strip().split(' ')

        for operators in itertools.product('+*|', repeat=len(parts) - 1):
            total = int(parts[0])
            for i in range(1, len(parts)):
                if operators[i - 1] == '+':
                    total += int(parts[i])
                elif operators[i - 1] == '*':
                    total *= int(parts[i])
                else:
                    total = int(str(total) + parts[i])

            if total == int(answer):
                expression = parts[0] + ''.join(
                    f' {operators[i]} {parts[i + 1]}'
                    for i in range(len(parts) - 1))
                print(f'{expression} = {total}')

                found += total
                break

print(found)
