from src.util.input_helpers import get_test_input_for_day
from AOC_scripts.year_2023.day_11_2023 import part_two, part_one, calculate_pair_wise_distances


def test_part_one():
    answer = part_one(get_test_input_for_day(2023, 11))
    assert answer == 374


def test_part_two():
    answer = part_two(get_test_input_for_day(2023, 11))
    assert answer is not None

    answer = calculate_pair_wise_distances(10, get_test_input_for_day(2023, 11))
    assert answer == 1030
