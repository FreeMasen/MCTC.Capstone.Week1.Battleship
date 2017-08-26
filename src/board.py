from src.grid import Grid
from src.cell_state import CellState
from src.direction import Direction

class Board():
    def __init__(self):
        self.defense = Grid(10, 10)
        self.offense = Grid(10,10)

    def place_ship(self, start_x, start_y, length, direction):
        for i in range(length):
            x = start_x + i if direction == Direction.Vertical else start_x
            y = start_y + i if direction == Direction.Horizontal else start_y
            self.defense.mark(x, y, CellState.Occupied)

    def bomb_square(self, x, y):
        if (self.check_square(x, y)):
            self.offense.mark(x, y, CellState.Hit)
        else:
            self.offense.mark(x, y, CellState.Missed)
    
    def check_square(self, x, y):
        if (self.defense[x][y] == 'S'):
            return True
        return False

    def display_defense(self):
        return self.defense.display()
    
    def display_offense(self):
        return self.offense.display()