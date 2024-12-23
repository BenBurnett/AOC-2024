import sys
from collections import defaultdict
from typing import Generator, List, Set, Callable
from itertools import combinations


def test_input() -> None:
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

    g = build_graph(_input)

    assert part_1(g) == 7
    assert part_2(g) == 'co,de,ka,ta'


class Graph:

    def __init__(self) -> None:
        self.graph = defaultdict(set)

    def add_edge(self, a: str, b: str) -> None:
        self.graph[a].add(b)
        self.graph[b].add(a)

    def _bron_kerbosch(self, r: Set[str], p: Set[str], x: Set[str]) -> Generator[Set[str], None, None]:
        if not p and not x:
            yield r
        else:
            pivot = next(iter(p | x))
            for v in p - self.graph[pivot]:
                yield from self._bron_kerbosch(r | {v}, p & self.graph[v], x & self.graph[v])
                p.remove(v)
                x.add(v)

    def cliques(self, condition: Callable[[Set[str]], bool] = lambda x: True) -> Generator[Set[str], None, None]:
        yield from (clique for clique in self._bron_kerbosch(set(), set(self.graph.keys()), set()) if condition(clique))


def read_input(path: str) -> List[str]:
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def build_graph(input_data: List[str]) -> Graph:
    g = Graph()
    for edge in input_data:
        g.add_edge(*edge.split('-'))
    return g


def part_1(g: Graph) -> int:
    cliques: Set[frozenset[str]] = set()

    for clique in g.cliques(lambda x: len(x) >= 3):
        cliques.update(frozenset(combo) for combo in combinations(clique, 3))

    return sum(1 for c in cliques if any(node.startswith('t') for node in c))


def part_2(g: Graph) -> str:
    return ','.join(sorted(max(g.cliques(), key=len)))


def main() -> None:
    input_data = read_input(sys.argv[1])
    g = build_graph(input_data)

    print(f'Part 1: {part_1(g)}')
    print(f'Part 2: {part_2(g)}')


if __name__ == "__main__":
    main()
