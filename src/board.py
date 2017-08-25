import Grid from grid.py
class Board():
    def __init__(self):
        self.left_grid = Grid(10, 10)
        self.right_grid = Grid(10,10)
    
    def bomb_square(self, )