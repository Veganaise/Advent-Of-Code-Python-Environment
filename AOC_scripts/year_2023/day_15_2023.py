import re
from typing import List

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


def hash(input: str, m=17, mod=256) -> int:
    v = 0
    for c in input:
        v += ord(c)
        v *= m
        v %= mod

    return v


@solution_timer(2023, 15, 1)
def part_one(input_data: List[str]):
    answer = sum(map(lambda x: hash(x), input_data[0].split(',')))

    if not answer:
        raise SolutionNotFoundException(2023, 15, 1)

    return answer


@solution_timer(2023, 15, 2)
def part_two(input_data: List[str]):
    boxes = [[] for _ in range(256)]
    p = re.compile(r'([a-z]+)([=|-])(\d)?')

    for instruction in p.findall(input_data[0]):
        label = instruction[0]
        hl = hash(label)
        if instruction[1] == '=':
            lens = (label, int(instruction[2]))
            v = list(i for i, v in enumerate(boxes[hl]) if v[0] == label)
            if v:
                boxes[hl][v[0]] = lens
            else:
                boxes[hl].append(lens)
        else:
            if boxes[hl]:
                v = list(v for v in boxes[hl] if v[0] == label)
                if v:
                    boxes[hl].remove(v[0])

    answer = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            focal_length = lens[1]
            answer += (i + 1) * (j + 1) * focal_length

    if not answer:
        raise SolutionNotFoundException(2023, 15, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 15)
    part_one(data)
    part_two(data)
