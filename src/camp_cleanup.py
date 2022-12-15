from dataclasses import dataclass
from itertools import starmap

from src.parser import read_lines


@dataclass
class Section:
    start: int = 0
    end: int = 0

    def contains(self, other):
        return self.start <= other.start and other.end <= self.end

    def overlaps(self, other):
        return (self.start <= other.start <= self.end) or \
               (other.start <= self.start <= other.end)


def pairs_completely_overlap(section1, section2):
    return section1.contains(section2) or section2.contains(section1)


def pairs_partially_overlap(section1, section2):
    return section1.overlaps(section2)


def num_completely_overlapping_sections(section_pairs):
    return sum(starmap(pairs_completely_overlap, section_pairs))


def num_partially_overlapping_sections(section_pairs):
    return sum(starmap(pairs_partially_overlap, section_pairs))


def parse_cleaning_sections(path):
    lines = read_lines(path)

    def parse_section(section_string):
        start, end = section_string.split('-')
        return Section(int(start), int(end))

    def parse_pair(pair_string):
        s1, s2 = pair_string.split(',')
        return parse_section(s1), parse_section(s2)

    return list(map(parse_pair, lines))
