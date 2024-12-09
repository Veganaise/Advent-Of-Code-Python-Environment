from typing import List

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


def is_safe(vals):
    is_increasing = True if vals[1] > vals[0] else False
    for i in range(1, len(vals)):
        diff = vals[i] - vals[i - 1]
        if ((is_increasing and diff < 0)
                or (not is_increasing and diff > 0)
                or diff == 0
                or abs(diff) > 3):
            return False
    return True


@solution_timer(2024, 2, 1)
def part_one(input_data: List[str]):
    answer = 0
    for line in input_data:
        vals = list(map(int, line.split()))
        if is_safe(vals):
            answer += 1

    if not answer:
        raise SolutionNotFoundException(2024, 2, 1)

    return answer


def is_safe_part_two(vals):
    diffs = [vals[i] - vals[i - 1] for i in range(1, len(vals))]
    increasing = len(list(filter(lambda x: x > 0, diffs)))
    if 1 < increasing < len(diffs) - 1:
        return False
    is_increasing = True
    if increasing <= 2:
        is_increasing = False

    nb_faults = len(list(filter(lambda x: x == 0
                                          or abs(x) > 3
                                          or (is_increasing and x < 0)
                                          or (not is_increasing and x > 0)
                                , diffs)))
    return nb_faults <= 1


@solution_timer(2024, 2, 2)
def part_two(input_data: List[str]):
    answer = 0

    def is_safe(nums, safe_range, allow_skip):
        prev = nums[0]
        for curr in nums[1:]:
            if curr - prev in safe_range:
                prev = curr
            elif not allow_skip:
                return False
            else:
                allow_skip = False
        return True

    increasing = range(1, 4)
    decreasing = range(-3, 0)
    for line in input_data:
        nums = [int(num) for num in line.split()]
        answer += any([
            is_safe(nums, increasing, True),
            is_safe(nums, decreasing, True),
            is_safe(nums[1:], increasing, False),
            is_safe(nums[1:], decreasing, False)
        ])

    if not answer:
        raise SolutionNotFoundException(2024, 2, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2024, 2)
    part_one(data)
    part_two(data)
