from src.util.input_helpers import get_test_input_for_day
from AOC_scripts.year_2023.day_08_2023 import part_two, part_one

data_p1="""LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

def test_part_one():
    answer = part_one(data_p1.splitlines())
    assert answer == 6


def test_part_two():
    answer = part_two(get_test_input_for_day(2023, 8))
    assert answer == 6
