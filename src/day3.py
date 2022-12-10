from src.rucksack import load_rucksacks, \
    find_common_rucksack_items_and_sum_them, find_badge_items, \
    sum_item_priorities


def day3():
    rucksacks = load_rucksacks('../input/day3_1.txt')
    sum_of_priorities = find_common_rucksack_items_and_sum_them(rucksacks)
    print(f"The sum of priorities is {sum_of_priorities}")

    badges = find_badge_items(rucksacks)
    sum_of_badges = sum_item_priorities(badges)
    print(f"The sum of the badges is {sum_of_badges}")


if __name__ == '__main__':
    day3()
