from src.board import Board
from src.grid import Grid
from src.cell_state import CellState
from src.direction import Direction
from src.player import Player
from src.ship import Ship
from src.game import Game
from src.data import Data
import inspect
from pyfiglet import Figlet

def main():
   
    g = Game()
    print(dir(g))
    print('\n')
    
    print_obj(g)
    # game = Game()
    # game.setup()
    # while not game.game_over:
    #     game.take_turn()

def print_obj(obj):
    for key in obj.__dict__:
        val = obj.__dict__[key]
        print('%s: %s' % (key, type(val)))
        

def banner():
    f = Figlet(font='trek')
    name = f.renderText('Battleship')
    lines = name.split('\n')
    width = len(lines[0])
    newLines = list()
    for line in lines:
        line = '│' + line  + '│'
    top = '┌' + ('─' * width) + '┐'
    lines.insert(0, top)
    bottom = '└' + ('─' * width) + '┘'
    lines.append(bottom)
    return '\n'.join(lines)
    


if __name__ == "__main__":
    main()