from data.models import *

import datetime
class Data():
    def __init__(self):
        self.db = db
        db.connect()
        db.create_tables([Game,Player, Board, Grid, Cell])
    
    def insert_game(self, game):
        db_game = Game()
        db_game.complete = False
        db_game.two_player = game.two_player
        db_game.start =  datetime.datetime.now()
        db_game.save()
        self.insert_player(db_game, game.player_one)
        self.insert_player(db_game, game.player_two)

    def insert_player(self, db_game, player):
        db_player = Player()
        db_player.game = db_game
        db_player.save()
        self.insert_board(db_player, player.board)

    def insert_board(self, db_player, board):
        db_board = Board()
        db_board.player = db_player
        db_board.save()
        self.insert_grid(db_board, board.offense, True)
        self.insert_board(db_board, board.defense, False)
    
    def insert_grid(self, db_board, grid, offense):
        db_grid = Grid()
        db_grid.board = db_board
        db_grid.offense = offense
        db_grid.save()
        for i in range(grid.width):
            for j in range(grid.height):
                self.insert_cell(db_grid, i, j, grid.cells[i][j].state)
    
    def insert_cell(self, db_grid, x, y, state):
        print(x, y, state)
        db_cell = Cell()
        db_cell.x = x
        db_cell.y = y
        db_cell.state = state
        db_cell.save()