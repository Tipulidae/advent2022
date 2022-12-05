from src.rock_paper_scissors import parse_moves, follow_guide, \
    parse_strategy


def test_day2_part1():
    guide = parse_moves('acceptance_tests/input/day2_1.txt')
    total_score = follow_guide(guide)
    assert total_score == 15


def test_day2_part2():
    guide = parse_strategy('acceptance_tests/input/day2_1.txt')
    total_score = follow_guide(guide)
    assert total_score == 12
