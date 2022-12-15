from src.camp_cleanup import pairs_completely_overlap, Section, \
    parse_cleaning_sections, pairs_partially_overlap


def test_pairs_completely_overlap_not_overlapping():
    assert not pairs_completely_overlap(Section(2, 4), Section(6, 8))
    assert not pairs_completely_overlap(Section(2, 3), Section(4, 5))
    assert not pairs_completely_overlap(Section(3, 7), Section(1, 5))


def test_pairs_completely_overlap():
    assert pairs_completely_overlap(Section(1, 1), Section(1, 1))
    assert pairs_completely_overlap(Section(2, 6), Section(3, 5))


def test_pairs_partially_overlap():
    assert pairs_partially_overlap(Section(1, 3), Section(2, 5))
    assert pairs_partially_overlap(Section(15, 50), Section(10, 30))
    assert pairs_partially_overlap(Section(1, 3), Section(3, 5))
    assert pairs_partially_overlap(Section(10, 13), Section(6, 10))
    assert pairs_partially_overlap(Section(1, 1), Section(1, 1))
    assert pairs_partially_overlap(Section(2, 6), Section(3, 5))
    assert pairs_partially_overlap(Section(3, 5), Section(2, 6))


# def test_pairs_partially_overlap_false():



def test_parse_cleaning_sections():
    section_pairs = parse_cleaning_sections(
        'acceptance_tests/input/day4_1.txt')
    expected = [
        (Section(2, 4), Section(6, 8)),
        (Section(2, 3), Section(4, 5)),
        (Section(5, 7), Section(7, 9)),
        (Section(2, 8), Section(3, 7)),
        (Section(6, 6), Section(4, 6)),
        (Section(2, 6), Section(4, 8)),
    ]
    assert section_pairs == expected
