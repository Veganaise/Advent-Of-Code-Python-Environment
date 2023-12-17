from src.util.input_helpers import get_test_input_for_day
from AOC_scripts.year_2023.day_16_2023 import part_two, part_one


def test_part_one():
    data = [
        ".|.",
        '.|-',
        ".-|"
    ]
    answer = part_one(data)
    assert answer == 7
    data = [
        "\\|.",
        '.|-',
        ".-|"
    ]
    answer = part_one(data)
    assert answer == 3

    answer = part_one(get_test_input_for_day(2023, 16))
    assert answer == 46


def test_part_two():
    answer = part_two(get_test_input_for_day(2023, 16))
    assert answer == 51
