from src.ship import Ship
from src.board import Board

class Player():
    def init(self):
        self.ships = dict(carrier = Ship(5), \
                        battleship = Ship(4), \
                        cruiser = Ship(3), \
                        submarine = Ship(3), \
                        destroyer = Ship(2))
        self.board = Board()
    
    def place_ship(self, ship_name, start_x, start_y, direction):
        ship = self.ships[ship_name]
        ship.start_x = start_x
        ship.start_y = start_y
        ship.direction = direction
        # self.board.place_ship(start_x, start_y, shi.length direction)
