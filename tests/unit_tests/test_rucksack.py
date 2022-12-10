from src.rucksack import Rucksack, item_priority, find_badge_items


class TestRucksack:
    def test_can_make_rucksack_with_two_compartments(self):
        compartment1 = 'vJrwpWtwJgWr'
        compartment2 = 'hcsFMMfFFhFp'
        items = compartment1 + compartment2
        rucksack = Rucksack(items)

        assert rucksack.compartment1 == compartment1
        assert rucksack.compartment2 == compartment2

    def test_find_common_item(self):
        items = 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
        rucksack = Rucksack(items)
        assert rucksack.common_item() == 'L'


def test_find_badge_items():
    items = [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw'
    ]
    rucksacks = list(map(Rucksack, items))
    badge_items = find_badge_items(rucksacks)
    assert badge_items == ['r', 'Z']


def test_lower_case_item_priority():
    item = 'f'
    assert item_priority(item) == 6


def test_upper_case_item_priority():
    item = 'C'
    assert item_priority(item) == 29

