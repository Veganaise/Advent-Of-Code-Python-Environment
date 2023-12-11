import itertools
from typing import List
import re

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


@solution_timer(2023, 11, 1)
def part_one(input_data: List[str]):
    expansion = 2

    answer = calculate_pair_wise_distances(expansion, input_data)

    if not answer:
        raise SolutionNotFoundException(2023, 11, 1)

    return answer


def calculate_pair_wise_distances(expansion, input_data):
    expansion -= 1
    n, m = len(input_data), len(input_data[0])
    empty_rows = list(range(n))
    empty_cols = list(range(m))
    stars = []
    for i in range(n):
        row = input_data[i]
        if '#' in row:
            empty_rows.remove(i)
        for match in re.finditer('#', row):
            j = match.start()
            stars.append([i, j])
            if j in empty_cols:
                empty_cols.remove(j)
    method_name(empty_cols, empty_rows, expansion, stars)
    pairwise_lengths = []
    for i1 in range(len(stars) - 1):
        for i2 in range(i1 + 1, len(stars)):
            if i1 == i2:
                continue
            s1 = stars[i1]
            s2 = stars[i2]
            l = abs(s1[0] - s2[0]) + abs(s1[1] - s2[1])
            pairwise_lengths.append(l)
    answer = sum(pairwise_lengths)
    return answer


def method_name(empty_cols, empty_rows, expansion, stars):
    for star in stars:
        star[0] += len([i for i in empty_rows if i < star[0]]) * expansion
        star[1] += len([j for j in empty_cols if j < star[1]]) * expansion


@solution_timer(2023, 11, 2)
def part_two(input_data: List[str]):
    expansion = 1000000

    answer = calculate_pair_wise_distances(expansion, input_data)

    if not answer:
        raise SolutionNotFoundException(2023, 11, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 11)
    part_one(data)
    part_two(data)
