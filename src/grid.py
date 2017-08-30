from src.cell import Cell
from src.consts import letters

class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #create a list the length of the height parameter 
        #filled with a list the length of the width parameter containing a cell
        self.cells = list(map(lambda row: list(map(lambda cell: Cell(), range(height))), range(width)))

    def mark(self, x, y, state):
        self.cells[y][x].state = state
    
    def check(self, x, y, desired_state):
        if (x >= self.width): return False
        if (y >= self.height): return False
        return self.cells[y][x].state == desired_state
    
    def display(self):
        ret = self.__table_top__() + '\n'
        for i in range(self.height - 1):
            ret += self.__row_string__(i) + '\n'
            ret += self.__row_border__() + '\n'
        ret += self.__row_string__(self.height - 1) + '\n'
        ret += self.__table_bottom__()
        return ret

    def __table_top__(self):
        ret = '     '
        for i in range(self.width):
            ret += '%s   ' % letters[i]
        ret += '\n'
        return ret + '   ┌' + ('───┬' * (self.width - 1)) + '───┐'

    def __row_border__(self):
        ret = '   ├'
        for i in range(self.width - 1):
            ret += '───┼'
        return ret + '───┤'

    def __row_string__(self, index): 
        ret = ''
        if (index < 9):
            ret += ' '
        ret += '%s │' % (index + 1)
        for cell in self.cells[index]:
            ret += ' %s │' % cell.display()
        return ret

    def __table_bottom__(self):
        return '   └' + ('───┴' * (self.width - 1)) + '───┘'