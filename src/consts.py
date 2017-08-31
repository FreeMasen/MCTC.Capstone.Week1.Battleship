import os
from pyfiglet import Figlet
#map of letters to indicies
numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
figlet = Figlet('rectangles', width=150)

# clear the terminal window
#https://stackoverflow.com/questions/2084508/clear-terminal-in-python
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wrap_in_box(text, width = None):
    lines = text.split('\n')
    if (width is None):
        width = max(map(lambda line: len(line), lines))
    newLines = list()
    newLines.append('╔' + ('═' * width) + '╗')
    for line in lines:
        if len(line.replace(' ', '')) > 0:
            newLines.append('║' + line.ljust(width)  + '║')
    newLines.append('╚' + ('═' * width) + '╝')
    return '\n'.join(newLines)

def side_by_side(left_banner, left_grid, right_banner, right_grid):
    left_text = left_banner.split('\n') + left_grid.split('\n')
    right_text = right_banner.split('\n') + right_grid.split('\n')
    left_width = max(map(lambda line: len(line), left_text))
    right_width = max(map(lambda line: len(line), right_text))
    left = list(map(lambda line: line.ljust(left_width), left_text))
    left_height = len(left)
    right_height = len(right_text)
    height = max(left_height, right_height)
    ret = ''
    for i in range(height):
        left_line = left[i] if i < left_height else ('' * left_width)
        right_line = right_text[i] if i < right_height else ('' * right_width)
        ret += '%s  %s\n' % (left_line, right_line)
    return ret