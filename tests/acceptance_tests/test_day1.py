from src.day1 import most_calories, parse_calories


def input_data():
    return parse_calories('acceptance_tests/input/day1_1.txt')


def test_day1_part1():
    calories = most_calories(input_data())
    assert calories == 24000


def test_day1_part2():
    calories = most_calories(input_data(), num_elves=3)
    assert calories == 45000
