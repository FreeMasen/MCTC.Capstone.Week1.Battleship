from src.ship import Ship
from src.board import Board

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
                print('%s, %s %s' % (name, ship.coordinates, (x, y)))
                ship.coordinates.index((x, y))
                if ship.mark_hit():
                    return 'You sunk my %s!' % name
                return 'Direct hit!'
            except:
                continue
    
    def has_lost(self):
        for ship in self.ships:
            if not ship.is_sunk:
                return False
        return True