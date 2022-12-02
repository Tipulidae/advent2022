from src.day1 import most_calories


def test_day1_part1():

    calories = most_calories('acceptance_tests/input/day1_1.txt')
    assert calories == 24000
