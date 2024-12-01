with open('input.txt') as f:
    lines = f.readlines()
    left, right = zip(*(map(int, line.split()) for line in lines))

left = sorted(left)
right = sorted(right)

difference = sum(abs(x - y) for x, y in zip(left, right))
print(difference)
