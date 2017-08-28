from src.board import Board
from src.grid import Grid
from src.cell_state import CellState
from src.direction import Direction
from src.player import Player
from src.ship import Ship
from src.game import Game
from pyfiglet import Figlet

def main():
    print(banner() + '\n')
    # game = Game()
    # game.setup()
    # while not game.game_over:
    #     game.take_turn()

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