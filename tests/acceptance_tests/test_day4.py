from src.camp_cleanup import num_completely_overlapping_sections, \
    parse_cleaning_sections, num_partially_overlapping_sections


def test_day4_part1():
    section_pairs = parse_cleaning_sections('acceptance_tests/input/day4_1.txt')
    num_overlaps = num_completely_overlapping_sections(section_pairs)
    assert num_overlaps == 2


def test_day4_part2():
    section_pairs = parse_cleaning_sections('acceptance_tests/input/day4_1.txt')
    num_partial_overlaps = num_partially_overlapping_sections(section_pairs)
    assert num_partial_overlaps == 4
