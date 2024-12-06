import re
from functools import reduce
from typing import List
import networkx as nx

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


@solution_timer(2023, 25, 1)
def part_one(input_data: List[str]):
    graph = nx.Graph()
    p = re.compile(r'(\w+)')
    for line in input_data:
        source, connected = line.split(':')
        connected = list(p.findall(connected))
        for n in connected:
            graph.add_edge(source, n)

    edges_to_remove = nx.minimum_edge_cut(graph)
    graph.remove_edges_from(edges_to_remove)

    group_sizes = [len(group) for group in nx.connected_components(graph)]
    answer = reduce(lambda x, y: x * y, group_sizes)

    if not answer:
        raise SolutionNotFoundException(2023, 25, 1)

    return answer


@solution_timer(2023, 25, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2023, 25, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 25)
    part_one(data)
    part_two(data)
