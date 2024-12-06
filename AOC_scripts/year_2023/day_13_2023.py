from typing import List

from src.util.exceptions import SolutionNotFoundException
from src.util.helpers import solution_timer
from src.util.input_helpers import get_input_for_day


class Pattern:
    def __init__(self):
        self.data = []

    def add_line(self, line):
        self.data.append(line)

    def find_reflection(self):
        n, m = len(self.data), len(self.data[0])
        for i in range(1, n):
            if self.check_reflection_at_row(i):
                return i * 100
        for j in range(1, m):
            if self.check_reflection_at_col(j):
                return j

    def find_reflection_part2(self):
        n, m = len(self.data), len(self.data[0])
        for i in range(1, n):
            if self.check_reflection_at_row_part2(i):
                return i * 100
        for j in range(1, m):
            if self.check_reflection_at_col_part2(j):
                return j

    def check_reflection_at_row(self, i: int):
        assert 0 < i <= len(self.data)
        before = list(reversed(self.data[:i]))
        after = self.data[i:]
        is_reflection = True
        for x in range(min(len(before), len(after))):
            if before[x] != after[x]:
                is_reflection = False
                break
        return is_reflection

    def check_reflection_at_col(self, j: int):
        assert 0 < j <= len(self.data[0])
        n, m = len(self.data), len(self.data[0])
        mid = min(j, m - j)
        is_reflection = True
        for x in range(1, mid + 1):
            for line in self.data:
                if line[j - x] != line[j + x - 1]:
                    is_reflection = False
                    break
        return is_reflection

    def check_reflection_at_row_part2(self, i: int):
        assert 0 < i <= len(self.data)
        m = len(self.data[0])
        before = list(reversed(self.data[:i]))
        after = self.data[i:]
        diffs = 0
        for x in range(min(len(before), len(after))):
            for y in range(m):
                if before[x][y] != after[x][y]:
                    diffs += 1
                    if diffs >= 2:
                        return False
        return diffs == 1

    def check_reflection_at_col_part2(self, j: int):
        assert 0 < j <= len(self.data[0])
        n, m = len(self.data), len(self.data[0])
        mid = min(j, m - j)
        diffs = 0
        for x in range(1, mid + 1):
            for line in self.data:
                if line[j - x] != line[j + x - 1]:
                    diffs += 1
                    if diffs >= 2:
                        return False
        return diffs == 1


@solution_timer(2023, 13, 1)
def part_one(input_data: List[str]):
    pattern = Pattern()
    patterns = []
    for line in input_data:
        if line == '':
            patterns.append(pattern)
            pattern = Pattern()
        else:
            pattern.add_line(line)
    patterns.append(pattern)

    answer = 0
    for p in patterns:
        answer += p.find_reflection()

    if not answer:
        raise SolutionNotFoundException(2023, 13, 1)

    return answer


@solution_timer(2023, 13, 2)
def part_two(input_data: List[str]):
    pattern = Pattern()
    patterns = []
    for line in input_data:
        if line == '':
            patterns.append(pattern)
            pattern = Pattern()
        else:
            pattern.add_line(line)
    patterns.append(pattern)

    answer = 0
    for p in patterns:
        answer += p.find_reflection_part2()

    if not answer:
        raise SolutionNotFoundException(2023, 13, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 13)
    part_one(data)
    part_two(data)
