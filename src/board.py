from src.grid import Grid
from src.cell_state import CellState
from src.direction import Direction

class Board():
    def __init__(self):
        self.defense = Grid(10, 10)
        self.offense = Grid(10, 10)

    def bomb_square(self, x, y):
        cell = self.defense.cells[y][x]
        if (cell.state == CellState.Occupied):
            self.defense.mark(x, y, CellState.Hit)
        if (cell.state == CellState.Open):
            self.defense.mark(x, y, CellState.Missed)
        else:
            return CellState.Invalid
        return cell.state

    def place_ship(self, ship):
        #for reversing
        history = list()
        #loop over the ship's coordinates
        for x, y in ship.coordinates:
            #if the cell is not open
            if not self.defense.check(x, y, CellState.Open):
                #reverse the current placements
                for rev_x, rev_y in history:
                    self.defense.mark(rev_x, rev_y, CellState.Open)
                #return false to indicate to the caller of the failure, ending the loop
                return False
            #add the placement to the history list and the grid
            self.defense.mark(x, y, CellState.Occupied)
            history.append((x, y))
        #return true to indicate success
        return True

    def remove_ship(self, ship):
        for i in range(ship.size):
            #set the x and y depending on the direction of the ship
            x = ship.start_x + i if ship.direction == Direction.Vertical else ship.start_x
            y = ship.start_y + i if ship.direction == Direction.Horizontal else ship.start_y
            self.defense.mark(x, y, CellState.Open)

    def display_defense(self):
        return self.defense.display()
    
    def display_offense(self):
        return self.offense.display()