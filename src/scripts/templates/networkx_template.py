from typing import List
import networkx as nx

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


@solution_timer(2023, 10, 1)
def part_one(input_data: List[str]):
    graph = nx.Graph()

    for line in input_data:
        node1, node2 = line.split()
        graph.add_edge(node1, node2)

    answer = ...

    if not answer:
        raise SolutionNotFoundException(2023, 10, 1)

    return answer


@solution_timer(2023, 10, 2)
def part_two(input_data: List[str]):
    graph = nx.Graph()
    
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2023, 10, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 10)
    part_one(data)
    part_two(data)
