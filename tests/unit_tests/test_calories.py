from src.calories import calories_per_elf
from src.day1 import sum_top_elves


def test_calories_per_elf():
    inp = [[1, 2, 3], [30, 10], [125]]
    expected = [6, 40, 125]
    assert calories_per_elf(inp) == expected


def test_sum_top_three_elves():
    inp = [1, 2, 3, 4]
    assert sum_top_elves(inp, num_elves=3) == 9


def test_sum_top_three_elves_unsorted_input():
    inp = [5, 1, 2, 3, 4]
    assert sum_top_elves(inp, num_elves=3) == 12
