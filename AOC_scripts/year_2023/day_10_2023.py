import math
from typing import List
import networkx as nx

from helpers.grid import Cardinals as d, Grid, iterate
from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day

pipes = {
    '-': (d.LEFT, d.RIGHT),
    '|': (d.UP, d.DOWN),
    '7': (d.LEFT, d.DOWN),
    'F': (d.RIGHT, d.DOWN),
    'J': (d.UP, d.LEFT),
    'L': (d.UP, d.RIGHT),
    '.': (),
    'S': (d.LEFT, d.UP, d.DOWN, d.RIGHT)
}


@solution_timer(2023, 10, 1)
def part_one(input_data: List[str]):
    graph = nx.Graph()

    source, _ = create_graph(graph, input_data)

    cycle = nx.find_cycle(graph, source=source)
    answer = math.ceil(len(cycle) / 2)

    if not answer:
        raise SolutionNotFoundException(2023, 10, 1)

    return answer


def create_graph(graph, input_data):
    grid = [[v for v in row] for row in input_data]
    grid = Grid(grid)
    source = None
    sources_dirs = set()
    for i, j, pipe in iterate(grid.grid):
        if pipe == 'S':
            source = (i, j)
        connection = pipes[pipe]
        for c in connection:
            val_in_dir = grid.value_in_direction(i, j, c)
            if val_in_dir:
                ni, nj, next_pipe = val_in_dir
                if d.opposite(c) in pipes[next_pipe]:
                    graph.add_edge((i, j), (ni, nj))
                    if pipe == 'S': sources_dirs.add(c.value)
    source_char = '.'
    if sources_dirs == {d.UP.value, d.DOWN.value}:
        source_char = '|'
    elif sources_dirs == {d.UP.value, d.LEFT.value}:
        source_char = 'J'
    elif sources_dirs == {d.UP.value, d.RIGHT.value}:
        source_char = 'L'
    elif sources_dirs == {d.DOWN.value, d.RIGHT.value}:
        source_char = 'F'
    elif sources_dirs == {d.UP.value, d.LEFT.value}:
        source_char = '7'
    elif sources_dirs == {d.LEFT.value, d.RIGHT.value}:
        source_char = '-'

    grid.grid[source[0]][source[1]] = source_char

    return source, grid


@solution_timer(2023, 10, 2)
def part_two(input_data: List[str]):
    graph = nx.Graph()

    source, grid = create_graph(graph, input_data)

    cycle = nx.find_cycle(graph, source=source)
    nodes_in_cycle = {node[0] for node in cycle}
    answer = 0
    for i, row in enumerate(grid.grid):
        b = False
        prev = ''
        for j, pipe in enumerate(row):
            if (i, j) in nodes_in_cycle:
                if pipe in '|':
                    b = not b
                if prev + pipe == 'FJ' or prev + pipe == 'L7':
                    b = not b
                if pipe in 'FJL7':
                    prev = pipe
            else:
                if b:
                    answer += 1

    if not answer:
        raise SolutionNotFoundException(2023, 10, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 10)
    part_one(data)
    part_two(data)
