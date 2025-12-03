from util.input import get_input

from itertools import combinations

def max_joltage(bank: str, batteries: int) -> str:
    # No possible joltage if there aren't enough batteries for it
    assert len(bank) >= batteries, "no possible max joltage"
    # The max joltage with a single battery is the bank's highest digit
    if batteries == 1:
        return max(bank)

    # Find highest first digit (leaving enough space for the rest of the
    # batteries)
    first_digit = max(bank[: -(batteries - 1)])
    # Combine that digit with the max joltage for the rest of the bank
    i = bank.index(first_digit)
    return first_digit + max_joltage(bank[i + 1 :], batteries - 1)

def part_1():
    
    puzzle_input = get_input(2025, 3).splitlines()
    puzzle_input = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()
    total = 0
    for row in puzzle_input:
        d1 = max(row[:-1])
        max_ind = row.index(d1)
        d2 = max(row[max_ind+1:])
        total += int(d1+d2)

    return total



def part_2():
    puzzle_input = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()

    comb_size = 2

    total = 0
    for row in puzzle_input:

        min_ind = 0
        max_vals = ''
        for i in range(comb_size, 0, -1):
            subset = row[min_ind:-i]
            print(row, subset, min_ind)
            max_val = max(subset)
            min_ind += subset.index(max_val) + 1
            max_vals += max_val
        print(max_vals)
        total += int(max_vals)

    return total
