from src.util.input_helpers import get_test_input_for_day
from AOC_scripts.year_2023.day_15_2023 import part_two, part_one, hash


def test_hash():
    assert hash('HASH') == 52
    assert hash('rn=1') == 30
    assert hash('pc=6') == 214


def test_part_one():
    answer = part_one(get_test_input_for_day(2023, 15))
    assert answer  == 1320


def test_part_two():
    answer = part_two(get_test_input_for_day(2023, 15))
    assert answer == 145
