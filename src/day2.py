from src.rock_paper_scissors import parse_moves, follow_guide, parse_strategy


def day2():
    strategy_guide = parse_moves('../input/day2_1.txt')
    total_score = follow_guide(strategy_guide)
    print(f"Total score is {total_score}")

    actual_guide = parse_strategy('../input/day2_1.txt')
    total_score = follow_guide(actual_guide)
    print(f"The real score is {total_score}")


if __name__ == '__main__':
    day2()
