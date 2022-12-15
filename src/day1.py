from src.calories import calories_per_elf
from src.parser import read_lines, split_to_sections, strings_to_int


def parse_calories(path):
    calories = split_to_sections(read_lines(path))
    return [strings_to_int(elf) for elf in calories]


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
