from src.calories import calories_per_elf


def parse_calories(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    calories = []
    elf = []
    for line in lines:
        if line == '\n':
            calories.append(elf)
            elf = []
            continue

        elf.append(int(line))

    return calories


def most_calories(path):
    data = parse_calories(path)
    summed_calories = calories_per_elf(data)
    return max(summed_calories)


def day1_part1():
    answer = most_calories('../input/day1_1.txt')
    print(f"The elf with the most calories had {answer} calories")


if __name__ == '__main__':
    day1_part1()
