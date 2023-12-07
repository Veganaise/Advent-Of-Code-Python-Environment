from src.util.input_helpers import get_test_input_for_day
from AOC_scripts.year_2023.day_07_2023 import part_two, part_one


def test_part_one():
    answer = part_one(get_test_input_for_day(2023, 7))
    assert answer == 6440


def test_part_two():
    answer = part_two(get_test_input_for_day(2023, 7))
    assert answer ==5905