from pyfiglet import Figlet
from src.grid import Grid
from src.consts import wrap_in_box

class Intro():
    def __init__(self):
        self.width = None

    def banner(self):
        f = Figlet(font='trek')
        name = f.renderText('Battleship')
        self.width = max(map(lambda line: len(line),name.split('\n') ))
        return wrap_in_box(name)

    def rules(self):
        grid = Grid(10, 10)
        steps = [
            'Each player get a total of 5 ships of varying lengths', \
            '    Carrier: 5', \
            '    Battleship: 4', \
            '    Cruiser: 3', \
            '    Submarine: 3', \
            '    Destroyer: 3', \
            'And a grid to place them on, it looks like this:', \
            grid.display(), \
            'I will ask you for the direction, x and y start for each of your ships', \
            'Once you have placed your ships the real fun begins', \
            'I will ask you for a set of coordinates that you would like to attack', \
            'if one of your opponent\'s ships is occupying that square, you will score a hit', \
            'Each ship can take as many hits as it is long', \
            'once a ship it reaches that maximum, it sinks', \
            'The first player to sink all of his/her opponents ships is the winner', \
            'Let\'s get started'
        ]
        return wrap_in_box('\n'.join(steps), self.width)