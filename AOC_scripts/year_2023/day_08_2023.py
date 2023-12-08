from typing import List
import re
from math import lcm

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


@solution_timer(2023, 8, 1)
def part_one(input_data: List[str]):
    instructions, nodes = extract_input(input_data)

    node = 'AAA'
    step = 0
    while node != 'ZZZ':
        inst = instructions[step % len(instructions)]
        i = 0 if inst == 'L' else 1
        node = nodes[node][i]
        step += 1

    answer = step

    if not answer:
        raise SolutionNotFoundException(2023, 8, 1)

    return answer


def extract_input(input_data):
    p = re.compile(r'([\d|A-Z]+)')
    nodes = {source: (l, r) for source, l, r in map(lambda x: p.findall(x), input_data[2:])}
    instructions = input_data[0]
    return instructions, nodes


@solution_timer(2023, 8, 2)
def part_two(input_data: List[str]):
    instructions, nodes = extract_input(input_data)
    starting_nodes = [v for v in nodes.keys() if v.endswith('A')]
    loops = []
    for sn in starting_nodes:
        node = sn
        step = 0
        while not node.endswith('Z'):
            inst = instructions[step % len(instructions)]
            i = 0 if inst == 'L' else 1
            node = nodes[node][i]
            step += 1
        loops.append(step)

    answer = lcm(*loops)

    if not answer:
        raise SolutionNotFoundException(2023, 8, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 8)
    part_one(data)
    part_two(data)
