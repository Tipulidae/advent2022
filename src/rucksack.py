from src.parser import read_lines


def find_common_rucksack_items_and_sum_them(rucksacks):
    common_items = [rucksack.common_item() for rucksack in rucksacks]
    return sum_item_priorities(common_items)


def sum_item_priorities(items):
    return sum(map(item_priority, items))


def load_rucksacks(path):
    lines = read_lines(path)
    return list(map(Rucksack, lines))


class Rucksack:
    def __init__(self, items):
        num_items = len(items)
        self.contents = items
        self.compartment1 = items[:num_items // 2]
        self.compartment2 = items[num_items // 2:]

    def common_item(self):
        return find_common_item([self.compartment1, self.compartment2])


def find_common_item(item_groups):
    return set.intersection(*map(string_to_set, item_groups)).pop()


def string_to_set(item_string):
    return {item for item in item_string}


def item_priority(item):
    ascii_value = ord(item)
    if ascii_value >= ord('a'):
        return ascii_value - ord('a') + 1
    else:
        return ascii_value - ord('A') + 27


def find_badge_items(rucksacks):
    items = []
    for i in range(len(rucksacks) // 3):
        contents = [r.contents for r in rucksacks[3 * i: 3 * i + 3]]
        badge_item = find_common_item(contents)
        items.append(badge_item)

    return items
