from enum import IntEnum
from itertools import starmap


class Shape(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    @property
    def score(self):
        return self + 1

    def wins_against(self, other):
        if (self - other) % 3 == 1:
            return True

        return False


def outcome_score(opponent, me):
    if opponent == me:
        return 3
    if opponent.wins_against(me):
        return 0
    else:
        return 6


def round_score(opponent, me):
    return me.score + outcome_score(opponent, me)


def parse_moves(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    return list(map(map_move, lines))


def parse_strategy(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    return list(map(map_strategy, lines))


def map_move(round_string):
    opponent, me = round_string.strip().split(' ')
    opponent_map = {
        'A': Shape.ROCK,
        'B': Shape.PAPER,
        'C': Shape.SCISSORS
    }
    me_map = {
        'X': Shape.ROCK,
        'Y': Shape.PAPER,
        'Z': Shape.SCISSORS
    }
    return opponent_map[opponent], me_map[me]


def follow_guide(strategy_guide):
    return sum(starmap(round_score, strategy_guide))


def map_strategy(round_string):
    opponent, outcome = round_string.strip().split(' ')
    opponent_map = {
        'A': Shape.ROCK,
        'B': Shape.PAPER,
        'C': Shape.SCISSORS
    }
    opponent_move = opponent_map[opponent]
    return opponent_move, my_move(opponent_move, outcome)


def my_move(opponent, outcome) -> Shape:
    if outcome == 'Y':
        return opponent
    direction = 1 if outcome == "Z" else -1
    return Shape((opponent + direction) % 3)
