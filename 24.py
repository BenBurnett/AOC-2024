import sys
from collections import deque


def test_input_1():
    _input = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02""".strip().split('\n')

    assert part_1(_input) == 4


def test_input_2():
    _input = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj""".strip().split('\n')

    assert part_1(_input) == 2024


def read_input(path: str) -> list[str]:
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def get_variables_and_gates(input_data: list[str]):
    variables = {}
    gates = []

    for line in input_data:
        if ':' in line:
            variable, value = line.split(': ')
            variables[variable] = int(value)
        elif '->' in line:
            a, op, b, _, c = line.split()
            gates.append((a, op, b, c))

    return variables, gates


def try_solve(variables: dict, gate: tuple[str, str, str, str]) -> bool:
    a, op, b, c = gate

    av = variables.get(a)
    bv = variables.get(b)

    if av is None or bv is None:
        return False

    if op == 'AND':
        variables[c] = av & bv
    elif op == 'OR':
        variables[c] = av | bv
    elif op == 'XOR':
        variables[c] = av ^ bv

    return True


class Graph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = {}

    def add_edge(self, node1, node2, description=""):
        self.add_node(node1)
        self.add_node(node2)
        self.nodes[node1][node2] = description
        self.nodes[node2][node1] = description


def part_1(input_data: list[str]):
    variables, gates = get_variables_and_gates(input_data)

    queue = deque(gates)

    while queue:
        gate = queue.popleft()
        if not try_solve(variables, gate):
            queue.append(gate)

    return int(''.join(str(variables[key]) for key in sorted(variables.keys(), reverse=True) if key.startswith('z')), 2)


def part_2(input_data: list[str]):
    _, gates = get_variables_and_gates(input_data)

    g = Graph()

    for gate in gates:
        a, op, b, c = gate
        g.add_edge(c, a, op)
        g.add_edge(c, b, op)

    swaps = set()
    for i in range(1, 45):
        x = f'x{i:02}'
        y = f'y{i:02}'
        z = f'z{i:02}'

        xors = next((k for k, v in g.nodes[x].items() if v == "XOR"), None)
        if not xors:
            continue
        next_xor = [k for k, v in g.nodes[xors].items() if v == "XOR"]

        if z not in next_xor:
            if len(next_xor) == 3:
                for n in next_xor:
                    if n != x and n != y:
                        swaps.update([z, n])
                        break
            else:
                nodes = list(g.nodes[x].keys())
                swaps.update(nodes[:2])

    return ','.join(sorted(swaps))


def main():
    input_data = read_input(sys.argv[1])
    print(f'Part 1: {part_1(input_data)}')
    print(f'Part 2: {part_2(input_data)}')


if __name__ == '__main__':
    main()
