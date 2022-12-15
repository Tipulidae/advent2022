from src.day5 import day5_part1


def test_day5_part1():
    top_crates = day5_part1('acceptance_tests/input/day5_1.txt')
    assert top_crates == 'CMZ'
