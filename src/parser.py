def read_lines(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return map(lambda line: line.strip('\n'), lines)


def split_to_sections(lines):
    list_of_sections = []
    section = []
    for line in lines:
        if line == '':
            list_of_sections.append(section)
            section = []
            continue

        section.append(line)
    list_of_sections.append(section)
    return list_of_sections


def strings_to_int(strings):
    return list(map(int, strings))
