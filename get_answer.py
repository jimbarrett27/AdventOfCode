import argparse
import importlib

parser = argparse.ArgumentParser(description='Get the solution for a given year and exercise')
parser.add_argument('year', type=int, help='The AoC year')
parser.add_argument('exercise_number', type=int, help='The exercise number')

# Parse the arguments
args = parser.parse_args()

module_name = f'{args.year}.ex_{args.exercise_number}'
module = importlib.import_module(module_name)

part_1_answer = getattr(module, 'part_1')()
part_2_answer = getattr(module, 'part_2')()

print(f'Part 1 answer: {part_1_answer}')
print(f'Part 2 answer: {part_2_answer}')