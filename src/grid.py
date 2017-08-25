class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #create a list the length of the height parameter 
        #filled with a list the length of the width parameter of the letter O
        self.cells = list(lambda row: list(lambda column: 'O', range(width)), range(height))

    def mark_ship(start_x, start_y, length, direction):
        i = 0
        if direction == 'horizontal':
            while (i < length):
                self.cells[start_x + i][start_y] = 'S'
        else:
            while(i < length):
                self.cells[start_x][start_y + i] = 'S'
    
    def attempt_to_hit(x, y):
