import sympy as sp
import re

x, y = sp.symbols('x y')
tokens = 0

with open('input.txt') as f:
    x_side = []
    y_side = []

    for line in f:
        line = line.strip()
        if line == '':
            continue

        a, b = re.findall(r'\d+', line)

        if 'Prize' in line:
            a = 10000000000000 + int(a)
            b = 10000000000000 + int(b)

        x_side.append(a)
        y_side.append(b)

        if len(x_side) == 3:
            eq1 = sp.Eq(int(x_side[0]) * x + int(x_side[1]) * y, int(x_side[2]))
            eq2 = sp.Eq(int(y_side[0]) * x + int(y_side[1]) * y, int(y_side[2]))

            solution = sp.solve((eq1, eq2), (x, y))
            if solution[x].is_integer and solution[y].is_integer:
                tokens += solution[x] * 3 + solution[y]

            x_side = []
            y_side = []

print(tokens)
