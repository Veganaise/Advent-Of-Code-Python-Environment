from src.util.input_helpers import get_test_input_for_day
from AOC_scripts.year_2023.day_13_2023 import part_two, part_one,Pattern

def test_pattern():
    p = Pattern()
    p.add_line('...#')
    p.add_line('...#')
    p.add_line('....')

    assert p.check_reflection_at_row(1)
    assert not p.check_reflection_at_row(2)

    assert p.check_reflection_at_col(1)
    assert not p.check_reflection_at_col(2)
    assert not p.check_reflection_at_col(3)


def test_part_one():
    answer = part_one(get_test_input_for_day(2023, 13))
    assert answer ==405


def test_part_two():
    answer = part_two(get_test_input_for_day(2023, 13))
    assert answer == 400
