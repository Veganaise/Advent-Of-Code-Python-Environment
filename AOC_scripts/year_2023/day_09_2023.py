import re
from typing import List

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


def derivate(nums: list[int]):
    return [nums[i] - nums[i - 1] for i in range(1, len(nums))]


@solution_timer(2023, 9, 1)
def part_one(input_data: List[str]):
    ans = process(input_data)

    answer = ans

    if not answer:
        raise SolutionNotFoundException(2023, 9, 1)

    return answer


def process(input_data, part2=False):
    p = re.compile(r'(-?\d+)')
    input_data = list(map(lambda x: list(map(int, p.findall(x))), input_data))
    ans = 0
    for nums in input_data:
        derivates = [nums]
        d = nums
        while set(d) != {0}:
            d = derivate(d)
            derivates.append(d)

        x = 0
        if part2:
            first = [x[0] for x in reversed(derivates)]
            for l in first[1:]:
                x = l - x
        else:
            last = [x[-1] for x in reversed(derivates)]
            for l in last[1:]:
                x += l

        ans += x
    return ans


@solution_timer(2023, 9, 2)
def part_two(input_data: List[str]):
    answer = process(input_data,part2=True)

    if not answer:
        raise SolutionNotFoundException(2023, 9, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 9)
    part_one(data)
    part_two(data)
