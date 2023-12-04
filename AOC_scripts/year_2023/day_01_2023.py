from typing import List

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day

import re


@solution_timer(2023, 1, 1)
def part_one(input_data: List[str]):
    p = re.compile(r'(\d)')

    def extract(line: str):
        occ = p.findall(line)
        return int(f'{occ[0]}{occ[-1]}')

    input_data = map(lambda line: extract(line), input_data)

    answer = sum(input_data)

    if not answer:
        raise SolutionNotFoundException(2023, 1, 1)

    return answer


dict_mapping = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ine': 9,
    'ight': 8,
    'ne': 1,
    'wo': 2,
    'hree': 3
}


@solution_timer(2023, 1, 2)
def part_two(input_data: List[str]):
    p = re.compile(r'(\d|(?<=o)ne|(?<=t)wo|(?<=t)hree|(?<=f)our|(?<=f)ive|(?<=s)ix|(?<=7)even|(?<=e)ight|('
                   r'?<=n)ine|one|two|three|four|five|six|seven|eight|nine)')

    def extract(line: str):
        occ = p.findall(line)
        return int(f'{dict_mapping[occ[0]]}{dict_mapping[occ[-1]]}')

    input_data = map(lambda line: extract(line), input_data)

    answer = sum(input_data)

    if not answer:
        raise SolutionNotFoundException(2023, 1, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 1)
    part_one(data)
    part_two(data)
