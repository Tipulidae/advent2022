from src.cargo_crane import parse_crates, follow_instructions


def day5_part1(path):
    cargo, instructions = parse_crates(path)
    follow_instructions(cargo, instructions)
    top_crates = cargo.top_crates()
    return top_crates


def day5():
    print(f"The top crates read: {day5_part1('../input/day5_1.txt')}")


if __name__ == '__main__':
    day5()
