from src.util.input_helpers import get_test_input_for_day
from AOC_scripts.year_2023.day_17_2023 import part_two, part_one,dirs


def test_dirs():
    assert {dirs.LEFT, dirs.UP, dirs.DOWN}.issubset(dirs.get_dirs_without_opposite(dirs.LEFT))
    assert {dirs.LEFT, dirs.UP, dirs.DOWN}.issuperset(dirs.get_dirs_without_opposite(dirs.LEFT))

def test_part_one_basics():
    data = [
        "12"
    ]
    answer = part_one(data)
    assert answer == 2

    data = [
        "12",
        "34"
    ]
    answer = part_one(data)
    assert answer == 6

    data = [
        "11111",
        "54321"
    ]
    answer = part_one(data)
    assert answer == 6


def test_part_one():
    answer = part_one(get_test_input_for_day(2023, 17))
    assert answer == 102




def test_part_two_base():
    data = ["111111111111",
            "999999999991",
            "999999999991",
            "999999999991",
            "999999999991"
            ]
    answer = part_two(data)
    assert answer == 71


def test_part_two():
    answer = part_two(get_test_input_for_day(2023, 17))
    assert answer == 94
