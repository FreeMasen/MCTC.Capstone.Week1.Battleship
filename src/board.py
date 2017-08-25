import Grid from grid.py
class Board():
    def __init__(self):
        self.defense = Grid(10, 10)
        self.offense = Grid(10,10)
    
    def bomb_square(self, x, y):
        self.offense.mark(x, y, 'B')
    
    def check_square(self, x, y):
        if (self.defense[x][y] == 'S'):
            return True
        return False

    def print_defense(self):
        self.defense.print()
    
    def print_offense(self):
        self.offense.print()