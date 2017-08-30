from src.ship import Ship
from src.board import Board
from src.consts import *
class Player():
    def __init__(self):
        self.board = Board()
        self.ships = dict()
        self.ships['carrier'] = Ship(5)
        self.ships['battleship'] = Ship(4)
        self.ships['cruiser'] = Ship(3)
        self.ships['submarine'] = Ship(3) 
        self.ships['destroyer'] = Ship(2)

    def mark_hit(self, x, y):
        for name, ship in self.ships.items():
            try:
                ship.coordinates.index((x, y))
                if ship.mark_hit():
                    return 'You sunk my %s!' % name
                return 'Direct hit!'
            except:
                continue
    
    def has_lost(self):
        for name, ship in self.ships.items():
            if not ship.is_sunk():
                return False
        return True

    def display_board(self):
        left_banner = figlet.renderText('Your Shots')
        left_grid = self.board.display_offense()
        right_banner = figlet.renderText('Your Ships')
        right_grid = self.board.display_defense()
        return side_by_side(left_banner, left_grid, right_banner, right_grid)