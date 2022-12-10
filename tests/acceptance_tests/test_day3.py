from src.rucksack import find_common_rucksack_items_and_sum_them, \
    load_rucksacks, sum_item_priorities, find_badge_items


def test_day3_part1():
    rucksacks = load_rucksacks('acceptance_tests/input/day3_1.txt')
    sum_of_priorities = find_common_rucksack_items_and_sum_them(rucksacks)
    assert sum_of_priorities == 157


def test_day3_part2():
    rucksacks = load_rucksacks('acceptance_tests/input/day3_1.txt')
    badges = find_badge_items(rucksacks)
    sum_of_priorities = sum_item_priorities(badges)
    assert sum_of_priorities == 70
