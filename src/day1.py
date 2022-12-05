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

    calories.append(elf)
    return calories


def most_calories(data, num_elves=1):
    summed_calories = calories_per_elf(data)
    return sum_top_elves(summed_calories, num_elves=num_elves)


def sum_top_elves(summed_calories, num_elves=1):
    if num_elves == 1:
        return max(summed_calories)

    return sum(sorted(summed_calories, reverse=True)[:num_elves])


def day1():
    data = parse_calories('../input/day1_1.txt')
    answer = most_calories(data)
    print(f"The elf with the most calories had {answer} calories")
    answer = most_calories(data, num_elves=3)
    print(f"The top three elves carry {answer} calories")


if __name__ == '__main__':
    day1()
