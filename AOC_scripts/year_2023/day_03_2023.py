import stringadd
from collections import defaultdict
from functools import reduce
from typing import List, DefaultDict

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


@solution_timer(2023, 3, 1)
def part_one(input_data: List[str]):
    n, m = len(input_data), len(input_data[0])
    i = 0
    row = None
    special_chars = set(string.punctuation) - {'.'}
    res = 0
    while i < n:
        prev_row = row if row else input_data[0]
        row = input_data[i]
        next_row = input_data[i + 1] if i != (n - 1) else row
        num = ''
        start_j = 0
        j = 0
        while j < m:
            if row[j].isnumeric():
                if num == '':
                    start_j = j
                num += row[j]
            elif num != '':
                res = check_if_part(j, m, next_row, num, prev_row, res, row, special_chars, start_j)
                num = ''
            j += 1
        if num != '':
            res = check_if_part(j, m, next_row, num, prev_row, res, row, special_chars, start_j)
            num = ''
        i += 1

    answer = res

    if not answer:
        raise SolutionNotFoundException(2023, 3, 1)

    return answer


def check_if_part(j, m, next_row, num, prev_row, res, row, special_chars, start_j):
    end_j = j
    start = start_j - 1 if start_j > 0 else 0
    end = end_j + 1 if end_j < m - 2 else end_j - 1
    neighbors = set(prev_row[start:end]).union(next_row[start:end]).union(
        {row[start],
         row[end - 1]
         })
    special_neighbors = special_chars.intersection(neighbors)
    if len(special_neighbors) >= 1:
        res += int(num)
    return res


def check_gear_and_return_coord(start_j, j, m, n, num, i, row, input_data, dict_gears):
    start = start_j - 1 if start_j > 0 else 0
    end = j + 1 if j < m - 2 else m - 1
    prev_row = i - 1 if i > 0 else 0
    next_row = i + 1 if i < n - 2 else n - 1
    neighbors_coord = [(prev_row, y) for y in range(start, end)]
    neighbors_coord.extend([(next_row, y) for y in range(start, end)])
    neighbors_coord.append((i, start))
    neighbors_coord.append((i, end - 1))
    for x, y in neighbors_coord:
        if input_data[x][y] == '*':
            dict_gears[(x, y)].append(int(num))
            if len(dict_gears[(x, y)]) == 2:
                return reduce(lambda a, b: a * b, dict_gears[(x, y)])
    return None


@solution_timer(2023, 3, 2)
def part_two(input_data: List[str]):
    n, m = len(input_data), len(input_data[0])
    i = 0
    row = None
    special_chars = set(string.punctuation) - {'.'}
    answer = 0
    dict_gears = defaultdict(list)
    while i < n:
        prev_row = row if row else input_data[0]
        row = input_data[i]
        next_row = input_data[i + 1] if i != (n - 1) else row
        num = ''
        start_j = 0
        j = 0
        while j < m:
            if row[j].isnumeric():
                if num == '':
                    start_j = j
                num += row[j]
            elif num != '':
                res = check_gear_and_return_coord(start_j, j, m, n, num, i, row, input_data, dict_gears)
                if res:
                    answer += res
                num = ''
            j += 1
        if num != '':
            res = check_gear_and_return_coord(start_j, j, m, n, num, i, row, input_data, dict_gears)
            if res: return res
            num = ''
        i += 1

    if not answer:
        raise SolutionNotFoundException(2023, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 3)
    part_one(data)
    part_two(data)
