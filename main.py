from src.board import Board
from src.grid import Grid
from src.cell_state import CellState
from src.direction import Direction
from src.player import Player
from src.ship import Ship
from src.game import Game

def main():
    game = Game()
    game.setup()
    while not game.game_over:
        game.take_turn()
        
if __name__ == "__main__":
    main()