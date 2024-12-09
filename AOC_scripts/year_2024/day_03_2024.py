import re
from typing import List

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


@solution_timer(2024, 3, 1)
def part_one(input_data: List[str]):
    input_data = ''.join(input_data)
    matches = re.findall(r'mul\((\d+),(\d+)\)', input_data)

    answer = sum([int(x[0]) * int(x[1]) for x in matches])

    if not answer:
        raise SolutionNotFoundException(2024, 3, 1)

    return answer


@solution_timer(2024, 3, 2)
def part_two(input_data: List[str]):
    input_data = ''.join(input_data)
    enabled = True
    answer = 0
    for m in re.finditer(r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)", input_data):
        m=m.group()
        if m == 'do()':
            enabled = True
        elif m == "don't()":
            enabled = False
        elif enabled:
            nums = re.findall(r"\d+", m)
            answer += int(nums[0]) * int(nums[1])

    if not answer:
        raise SolutionNotFoundException(2024, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2024, 3)
    part_one(data)
    part_two(data)
