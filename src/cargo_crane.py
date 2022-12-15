from dataclasses import dataclass

from src.parser import read_lines, split_to_sections


def parse_crates(path):
    lines = read_lines(path)
    sections = split_to_sections(lines)
    cargo = parse_cargo(sections[0])

    instructions = []
    for line in sections[1]:
        instructions.append(
            generate_instruction(*parse_instruction(line))
        )

    return cargo, instructions


def follow_instructions(crates, instructions):
    for instruction in instructions:
        instruction(crates)


def generate_instruction(origin, destination, times):
    def instruction(cargo):
        for _ in range(times):
            cargo.move_crate(origin, destination)

        return cargo

    return instruction


@dataclass
class Cargo:
    def __init__(self, *stacks):
        self.stacks = stacks

    def move_crate(self, origin, destination):
        crate = self.stacks[origin].pop()
        self.stacks[destination].append(crate)

    def top_crates(self):
        return ''.join([stack[-1] for stack in self.stacks])

    def __eq__(self, other):
        return self.stacks == other.stacks

    def __str__(self):
        return str(self.stacks)


def parse_cargo(lines):
    num_stacks = int((len(lines[0]) + 1) / 4)
    stacks = []
    for _ in range(num_stacks):
        stacks.append([])

    for line in lines[:-1]:
        for i, stack in enumerate(stacks):
            box = line[1 + i * 4]
            if box != ' ':
                stack.append(box)

    stacks = [list(reversed(stack)) for stack in stacks]
    return Cargo(*stacks)


def parse_instruction(instruction_string):
    words = instruction_string.split(" ")
    return (
        int(words[3]) - 1,
        int(words[5]) - 1,
        int(words[1])
    )
