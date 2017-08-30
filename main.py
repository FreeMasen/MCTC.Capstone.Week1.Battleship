from src.board import Board
from src.grid import Grid
from src.cell_state import CellState
from src.direction import Direction
from src.player import Player
from src.ship import Ship
from src.game import Game

def main():
    game = Game()
    game.__check_for_continue__()
    game.welcom_user()
    next_game = True
    while next_game:
        game.setup()
        while game.take_turn():
            pass
        next_game = game.play_again()
    game.exit()

if __name__ == "__main__":
    main()