class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #create a list the length of the height parameter 
        #filled with a list the length of the width parameter of the letter O
        self.cells = list(lambda row: list(lambda column: 'O', range(width)), range(height))

    def mark(self, x, y, char):
        self.cells[x][y] =  char
        i = 0
        if direction == 'horizontal':
            while (i < length):
                self.cells[start_x + i][start_y] = 'S'
        else:
            while(i < length):
                self.cells[start_x][start_y + i] = 'S'
    
    def print(self):
        pass