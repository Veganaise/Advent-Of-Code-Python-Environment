from dataclasses import dataclass
from functools import cache
from typing import List

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


@dataclass(frozen=True)
class arrangement:
    record: str
    damaged_groups: tuple

    @cache
    def get_count(self, char_idx: int, curr_group_idx: int, curr_group_len: int):
        count = 0
        if char_idx == len(self.record):
            if curr_group_idx == len(self.damaged_groups) and curr_group_len == 0:
                return 1
            elif (curr_group_idx == len(self.damaged_groups) - 1
                  and self.damaged_groups[curr_group_idx] == curr_group_len):
                return 1
            else:
                return 0

        for char in ('.', '#'):
            if self.record[char_idx] in (char, '?'):
                if char == '.':
                    if curr_group_len == 0:
                        count += self.get_count(char_idx + 1, curr_group_idx, 0)
                    elif (curr_group_idx < len(self.damaged_groups)) and (
                            curr_group_len == self.damaged_groups[curr_group_idx]):
                        count += self.get_count(char_idx + 1, curr_group_idx + 1, 0)
                else:
                    count += self.get_count(char_idx + 1, curr_group_idx, curr_group_len + 1)

        return count


@solution_timer(2023, 12, 1)
def part_one(input_data: List[str]):
    answer = 0
    for line in input_data:
        string, record = line.split(' ')
        record = tuple([int(x) for x in record.split(',')])
        arg = arrangement(string, record)
        c = arg.get_count(0, 0, 0)
        answer += c

    if not answer:
        raise SolutionNotFoundException(2023, 12, 1)

    return answer


@solution_timer(2023, 12, 2)
def part_two(input_data: List[str]):
    answer = 0
    for line in input_data:
        string, record = line.split(' ')
        string = '?'.join([string for _ in range(5)])
        record = ','.join([record for _ in range(5)])
        record = tuple([int(x) for x in record.split(',')])

        arg = arrangement(string, record)
        c = arg.get_count(0, 0, 0)
        answer += c

    if not answer:
        raise SolutionNotFoundException(2023, 12, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 12)
    part_one(data)
    part_two(data)
