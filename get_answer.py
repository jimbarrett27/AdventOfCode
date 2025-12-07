import argparse
import importlib
from time import perf_counter
import math

def round_sig(x, sig=3):
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

parser = argparse.ArgumentParser(description='Get the solution for a given year and exercise')
parser.add_argument('year', type=int, help='The AoC year')
parser.add_argument('exercise_number', type=int, help='The exercise number')

# Parse the arguments
args = parser.parse_args()

module_name = f'{args.year}.ex_{args.exercise_number}'
module = importlib.import_module(module_name)

start = perf_counter()
part_1_answer = getattr(module, 'part_1')()
part_1_time = round_sig(perf_counter() - start, 3)
start = perf_counter()
part_2_answer = getattr(module, 'part_2')()
part_2_time = round_sig(perf_counter() - start, 3)

print(f'Part 1 answer: {part_1_answer} time: {part_1_time}')
print(f'Part 2 answer: {part_2_answer} time: {part_2_time}')