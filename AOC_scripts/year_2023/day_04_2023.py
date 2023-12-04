import re
from typing import List

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


@solution_timer(2023, 4, 1)
def part_one(input_data: List[str], nb_winning_numbers=10):
    p = re.compile(r'(\d+)')

    def extract(line: str):
        match = p.findall(line)
        stop_at = nb_winning_numbers + 1
        winning_numbers = set(match[1:stop_at]).intersection(match[stop_at:])
        return 2 ** (len(winning_numbers) - 1) if len(winning_numbers) > 0 else 0

    answer = sum(map(lambda l: extract(l), input_data))

    if not answer:
        raise SolutionNotFoundException(2023, 4, 1)

    return answer


@solution_timer(2023, 4, 2)
def part_two(input_data: List[str], nb_winning_numbers=10):
    n = len(input_data)
    dp = [0]
    dp.extend([1 for _ in range(n)])
    p = re.compile(r'(\d+)')

    for line in input_data:
        match = p.findall(line)
        stop_at = nb_winning_numbers + 1
        card_id = int(match[0])
        winning_numbers = set(match[1:stop_at]).intersection(match[stop_at:])
        nb_points = len(winning_numbers)
        nb_cards = dp[card_id]

        for j in range(1, nb_points + 1):
            dp[card_id + j] += nb_cards

    answer = sum(dp)

    if not answer:
        raise SolutionNotFoundException(2023, 4, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 4)
    part_one(data)
    part_two(data)
