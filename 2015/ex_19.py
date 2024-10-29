from util.input import get_input
from collections import defaultdict

def part_1():
    
    puzzle_input = get_input(2015, 19)

    mappings = defaultdict(list)
    for line in puzzle_input.splitlines():

        if '=>' in line:
            source, dest = line.split('=>')
            mappings[source.strip()].append(dest.strip())

        else:
            medicine = line.strip()

    possible_molecules = set()
    for source, dests in mappings.items():

        source_len = len(source)
        for i in range(len(medicine) - source_len):
            if medicine[i: i+source_len] == source:
                for dest in dests:
                    possible_molecules.add(medicine[:i] + dest + medicine[i+source_len:])

    return len(possible_molecules)

def part_2():
    pass