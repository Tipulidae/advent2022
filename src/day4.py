from src.camp_cleanup import parse_cleaning_sections, \
    num_completely_overlapping_sections, num_partially_overlapping_sections


def day4():
    section_pairs = parse_cleaning_sections('../input/day4_1.txt')
    num_overlaps = num_completely_overlapping_sections(section_pairs)
    print(f"Number of completely overlapping cleaning sections is "
          f"{num_overlaps}")

    partial_overlaps = num_partially_overlapping_sections(section_pairs)
    print(f"Number of partially overlapping cleaning sections is "
          f"{partial_overlaps}")


if __name__ == '__main__':
    day4()
