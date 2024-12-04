from util.input import get_input
import re

def part_1():
    puzzle_input = get_input(2016, 9).strip()

    repetition_command = ''
    decompressed_string = ''
    making_command = False

    inp = puzzle_input

    i=0
    while i < len(inp):

        c = inp[i]

        if c == '(':
            making_command = True
        elif making_command and c == ')':
            making_command = False
            n_chars, n_reps = map(int, repetition_command.split('x'))
            decompressed_string += inp[i+1:i+n_chars+1] * n_reps
            repetition_command = ''
            i += n_chars
        elif making_command:
            repetition_command += c
        else:
            decompressed_string += c

        i += 1


    return len(decompressed_string)

def part_2():
    
    puzzle_input = get_input(2016, 9).strip()

    inp = puzzle_input

    i = len(inp) - 1

    def _has_decompression_instruction(s):
        return re.match(r'\(\d+x\d+\)')



    def _get_decompressed_length(s):

        if not _has_decompression_instruction(s):
            return len(s)

        making_command = False
        repetition_command = ''
        decompressed_length = 0
        i=0
        while i < len(inp):

            c = inp[i]

            if c == '(':
                making_command = True
            elif making_command and c == ')':
                making_command = False
                n_chars, n_reps = map(int, repetition_command.split('x'))
                affected_chars = inp[i+1:i+n_chars+1]
                repetition_command = ''
                i += n_chars
            elif making_command:
                repetition_command += c
            else:
                decompressed_length += 1

            i += 1
