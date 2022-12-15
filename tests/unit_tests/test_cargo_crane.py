from src.cargo_crane import Cargo, generate_instruction, follow_instructions, \
    parse_cargo, parse_instruction


def test_move_crate():
    cargo = Cargo(['Z', 'N'], ['M', 'C', 'D'], ['D'])
    cargo.move_crate(origin=1, destination=2)
    assert cargo == Cargo(['Z', 'N'], ['M', 'C'], ['D', 'D'])


def test_follow_instructions():
    cargo = Cargo(['Z', 'N'], ['M', 'C', 'D'], ['D'])
    instruction = generate_instruction(1, 2, 2)
    follow_instructions(cargo, [instruction])
    assert cargo == Cargo(['Z', 'N'], ['M'], ['D', 'D', 'C'])


def test_top_crates():
    cargo = Cargo(['Z', 'N'], ['M', 'C', 'D'], ['D'])
    assert cargo.top_crates() == 'NDD'


def test_parse_cargo_one_stack():
    inp = [
        "[A]",
        " 1 "
    ]
    assert parse_cargo(inp) == Cargo(['A'])


def test_parse_cargo():
    inp = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
    ]
    expected = Cargo(['Z', 'N'], ['M', 'C', 'D'], ['P'])
    assert parse_cargo(inp) == expected


def test_parse_instruction():
    assert parse_instruction("move 1 from 3 to 4") == (2, 3, 1)
