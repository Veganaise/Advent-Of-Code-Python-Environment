from typing import List
import re

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


def mapping(mappings: List, entries: set):
    output = set()
    for dest_start, source_start, range_size in mappings:
        offset = dest_start - source_start
        concerned = {e for e in entries if source_start <= e <= source_start + range_size}
        output = output.union({e + offset for e in concerned})
        entries.difference_update(concerned)

    return output.union(entries)


@solution_timer(2023, 5, 1)
def part_one(input_data: List[str]):
    p = re.compile(r'(\d+)')
    entries = {int(x) for x in p.findall(input_data[0])}
    input_data = input_data[3:]

    for _ in range(7):
        index_next_sep = input_data.index('')
        print(index_next_sep, input_data[index_next_sep])
        mappings = list(map(lambda x: [int(y) for y in p.findall(x)], input_data[:index_next_sep]))
        entries = mapping(mappings, entries)
        print(entries)
        input_data = input_data[index_next_sep + 2:]

    answer = min(entries)

    if not answer:
        raise SolutionNotFoundException(2023, 5, 1)

    return answer


class ItemRange():
    def __init__(self, start, size):
        self.low = start
        self.high = start + size - 1

    def apply_mapping(self, mappings: List, entries: set):
        for m in mappings:
            mlow = mapping(mappings, {self.low})
            mhigh = mapping(mappings, {self.low})


@solution_timer(2023, 5, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2023, 5, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 5)
    part_one(data)
    part_two(data)
