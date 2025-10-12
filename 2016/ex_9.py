import re
from util.input import get_input

def part_1():

    data = get_input(2016, 9)

    decompressed = ''
    ind = 0
    while True:
        c = data[ind]

        if c == '(':
            marker_text = ''
            while c != ')':
                ind += 1
                c = data[ind]
                marker_text += c
            
            n_chars, n_repeats = map(int, marker_text[:-1].split('x'))
            text_to_repeat = ''
            for _ in range(n_chars):
                ind += 1
                text_to_repeat += data[ind]
            
            decompressed += text_to_repeat * n_repeats


        else:
            decompressed += c    

        ind += 1

        if ind == len(data):
            break

    return len(decompressed)

def part_2():
    pass