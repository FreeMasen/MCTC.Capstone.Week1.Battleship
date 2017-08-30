from src.direction import Direction

class Ship():
    def __init__(self, size):
        self.size = size
        self.hits = 0
        self.placed = False
        self.direction = None
        self.coordinates = list()
    
    def place(self, start_x, start_y, direction):
        self.direction = direction
        for i in range(self.size):
            x = start_x + i if direction == Direction.Horizontal else start_x
            y = start_y + i if direction == Direction.Vertical else start_y
            self.coordinates.append((x, y))
            self.placed = True
    
    def mark_hit(self):
        self.hits += 1
        return self.is_sunk()

    def clear_placement(self):
        self.coordinates = list()
        self.placed = False

    def is_sunk(self):
        return self.size <= self.hits