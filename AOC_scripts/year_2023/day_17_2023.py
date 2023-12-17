from enum import Enum
from typing import List
import networkx as nx

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


class dirs(Enum):
    LEFT: tuple = (0, -1)
    UP: tuple = (-1, 0)
    RIGHT: tuple = (0, 1)
    DOWN: tuple = (1, 0)

    @staticmethod
    def get_dirs():
        return [dirs.LEFT, dirs.RIGHT, dirs.DOWN, dirs.UP]

    @staticmethod
    def get_dirs_without_opposite(d):
        return set({dirs.LEFT, dirs.RIGHT, dirs.DOWN, dirs.UP} - {d, opposites[d]})


opposites = {
    dirs.LEFT: dirs.RIGHT,
    dirs.RIGHT: dirs.LEFT,
    dirs.UP: dirs.DOWN,
    dirs.DOWN: dirs.UP
}


@solution_timer(2023, 17, 1)
def part_one(input_data: List[str]):
    graph = nx.DiGraph()
    n, m = len(input_data), len(input_data[0])

    for i in range(n):
        for j in range(m):
            for l in range(4):
                for d in dirs.get_dirs():
                    node = (i, j, l, d)
                    graph.add_node(node)

    for node in graph.nodes:
        i, j, l, d = node
        for direction in dirs.get_dirs_without_opposite(d):
            dx, dy = direction.value
            i_off, j_off = i + dx, j + dy
            cost = 0
            offset = l if direction == d else 0
            while offset <= 2 and 0 <= i_off < n and 0 <= j_off < m:
                next_node = (i_off, j_off, offset + 1, direction)
                cost += int(input_data[i_off][j_off])
                graph.add_weighted_edges_from([(node, next_node, cost)])

                offset += 1
                i_off += dx
                j_off += dy

    start_nodes = [((0, 0), u, 0) for u in graph.nodes if u[0] == 0 and u[1] == 0 and u[2] == 0]
    end_nodes = [(u, (n - 1, m - 1), 0) for u in graph.nodes if u[0] == n - 1 and u[1] == m - 1]

    graph.add_weighted_edges_from(start_nodes)
    graph.add_weighted_edges_from(end_nodes)

    answer = nx.shortest_paths.shortest_path_length(graph, (0, 0), (n - 1, m - 1), weight="weight")

    if not answer:
        raise SolutionNotFoundException(2023, 17, 1)

    return answer


@solution_timer(2023, 17, 2)
def part_two(input_data: List[str]):
    graph = nx.DiGraph()
    n, m = len(input_data), len(input_data[0])

    for i in range(n):
        for j in range(m):
            for d in dirs.get_dirs():
                node = (i, j, d)
                graph.add_node(node)

    for node in graph.nodes:
        i, j, d = node
        for direction in dirs.get_dirs_without_opposite(d):
            dx, dy = direction.value
            i_off, j_off = i, j
            cost = 0
            offset = 0
            while offset < 10 and 0 <= i_off + dx < n and 0 <= j_off + dy < m:

                offset += 1
                i_off += dx
                j_off += dy
                cost += int(input_data[i_off][j_off])
                if offset < 4:
                    continue
                next_node = (i_off, j_off, direction)
                if next_node not in graph.nodes:
                    print(next_node)

                graph.add_weighted_edges_from([(node, next_node, cost)])

    start_nodes = [((0, 0), u, 0) for u in graph.nodes if u[0] == 0 and u[1] == 0]
    end_nodes = [(u, (n - 1, m - 1), 0) for u in graph.nodes if u[0] == n - 1 and u[1] == m - 1]

    graph.add_weighted_edges_from(start_nodes)
    graph.add_weighted_edges_from(end_nodes)

    answer = nx.shortest_paths.shortest_path_length(graph, (0, 0), (n - 1, m - 1), weight="weight")

    if not answer:
        raise SolutionNotFoundException(2023, 17, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 17)
    part_one(data)
    part_two(data)
