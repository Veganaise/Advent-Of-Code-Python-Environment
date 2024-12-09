from src.util.input_helpers import get_test_input_for_day
from AOC_scripts.year_2024.day_02_2024 import part_two, part_one


def test_part_one():
    answer = part_one(get_test_input_for_day(2024, 2))
    assert answer is not None


def test_part_two():
    answer = part_two(get_test_input_for_day(2024, 2))
    assert answer == 4
    assert answer is not None
