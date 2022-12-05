from src.rock_paper_scissors import outcome_score, round_score, \
    parse_moves, map_move, my_move, parse_strategy, Shape


def test_outcome_score_win():
    winning_moves = zip(
        [Shape.ROCK, Shape.PAPER, Shape.SCISSORS],
        [Shape.PAPER, Shape.SCISSORS, Shape.ROCK]
    )
    for opponent, me in winning_moves:
        assert outcome_score(opponent, me) == 6


def test_outcome_score_loss():
    winning_moves = zip(
        [Shape.PAPER, Shape.SCISSORS, Shape.ROCK],
        [Shape.ROCK, Shape.PAPER, Shape.SCISSORS]
    )
    for opponent, me in winning_moves:
        assert outcome_score(opponent, me) == 0


def test_outcome_score_draw():
    for move in Shape:
        assert outcome_score(move, move) == 3


def test_round_score_rock_paper():
    assert round_score(Shape.ROCK, Shape.PAPER) == 8


def test_round_score_rock_scissors():
    assert round_score(Shape.ROCK, Shape.SCISSORS) == 3


def test_parse_moves():
    guide = parse_moves('acceptance_tests/input/day2_1.txt')
    expected = [
        (Shape.ROCK, Shape.PAPER),
        (Shape.PAPER, Shape.ROCK),
        (Shape.SCISSORS, Shape.SCISSORS)
    ]
    assert guide == expected


def test_parse_strategy():
    guide = parse_strategy('acceptance_tests/input/day2_1.txt')
    expected = [
        (Shape.ROCK, Shape.ROCK),
        (Shape.PAPER, Shape.ROCK),
        (Shape.SCISSORS, Shape.ROCK)
    ]
    assert guide == expected


def test_map_move():
    assert map_move("A Y") == (Shape.ROCK, Shape.PAPER)


def test_map_another_move():
    assert map_move("C X") == (Shape.SCISSORS, Shape.ROCK)


def test_my_move():
    me = my_move(Shape.ROCK, 'Z')
    assert me == Shape.PAPER


def test_my_other_move():
    me = my_move(Shape.ROCK, 'X')
    assert me == Shape.SCISSORS

