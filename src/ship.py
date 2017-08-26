from src.direction import Direction

class Ship():
    def __init__(self, size):
        self.size = size
        self.hits = 0
        self.placed = False
        self.start_x = None
        self.start_y = None
        self.direction = None
    
    def is_sunk(self):
        return self.size >= self.hits