from collections import Counter

with open('input.txt') as f:
    lines = f.readlines()
    left, right = zip(*(map(int, line.split()) for line in lines))

left = Counter(left)
right = Counter(right)

total = sum(k * right.get(k, 0) * v for k, v in left.items())
print(total)
