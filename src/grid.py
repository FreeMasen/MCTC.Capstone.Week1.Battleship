from src.cell import Cell
class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #create a list the length of the height parameter 
        #filled with a list the length of the width parameter containing a cell
        self.cells = list(map(lambda row: list(map(lambda cell: Cell(), range(height))), range(width)))

    def mark(self, x, y, state):
        self.cells[x][y].state = state
    
    def display(self):
        ret = self.__table_top__() + '\n'
        for i in range(self.height - 1):
            ret += self.__row_string__(i) + '\n'
            ret += self.__row_border__() + '\n'
        ret += self.__row_string__(self.height - 1) + '\n'
        ret += self.__table_bottom__()
        return ret

    def __table_top__(self):
        ret = '    '
        for i in range(self.width):
            ret += '%s   ' % i
        ret += '\n'
        return ret + '  ┌' + ('───┬' * (self.width - 1)) + '───┐'

    def __row_border__(self):
        ret = '  ├'
        for i in range(self.width - 1):
            ret += '───┼'
        return ret + '───┤'

    def __row_string__(self, index): 
        ret = '%s │' % index
        for cell in self.cells[index]:
            ret += ' %s │' % cell.display()
        return ret

    def __table_bottom__(self):
        return '  └' + ('───┴' * (self.width - 1)) + '───┘'