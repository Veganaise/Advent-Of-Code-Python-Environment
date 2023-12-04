import re
from collections import defaultdict
from functools import reduce
from typing import List

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day

max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}


@solution_timer(2023, 2, 1)
def part_one(input_data: List[str]):
    p = re.compile(r'(\d+) ([a-z]+)')
    res = []
    for line in input_data:
        game_id, cubes = line.split(': ')
        game_id = int(game_id.split()[-1])
        valid = True
        for nb, color in p.findall(line):
            if color in max_cubes.keys() and int(nb) > max_cubes[color]:
                valid = False
                break
        if valid:
            res.append(game_id)

    answer = sum(res)

    if not answer:
        raise SolutionNotFoundException(2023, 2, 1)

    return answer


@solution_timer(2023, 2, 2)
def part_two(input_data: List[str]):
    p = re.compile(r'(\d+) ([a-z]+)')
    res = []
    for line in input_data:
        game_id, cubes = line.split(': ')
        min_cubes = defaultdict(lambda: 0)
        for nb, color in p.findall(line):
            min_cubes[color] = max(int(nb), min_cubes[color])
        res.append(reduce(lambda x, y: x * y, min_cubes.values()))

    answer = sum(res)

    if not answer:
        raise SolutionNotFoundException(2023, 2, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 2)
    part_one(data)
    part_two(data)
