import sys

import networkx as nx


def test_input():
    _input = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""".strip().split("\n")

    edges = get_links(_input)

    g = nx.Graph()
    for edge in edges:
        g.add_edge(*edge)

    assert part_1(g) == 7
    assert part_2(g) == 'co,de,ka,ta'


def read_input(path: str) -> list[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def get_links(input_data: list[str]) -> set[frozenset[str]]:
    return set(frozenset(line.split('-')) for line in input_data)


def part_1(g: nx.Graph) -> int:
    triples: set[set[str]] = set()
    for source, target in g.edges:
        for p in nx.all_simple_paths(g, source, target, cutoff=2):
            if len(p) == 3:
                triples.add(frozenset(p))

    return sum(1 for group in triples if any(node.startswith('t') for node in group))


def part_2(g: nx.Graph) -> str:
    longest = []
    for c in nx.find_cliques(g):
        if len(c) > len(longest):
            longest = c
    return ','.join(sorted(longest))


def main():
    input_data = read_input(sys.argv[1])
    edges = get_links(input_data)

    g = nx.Graph()
    for edge in edges:
        g.add_edge(*edge)

    print(f'Part 1: {part_1(g)}')
    print(f'Part 2: {part_2(g)}')


if __name__ == '__main__':
    main()
