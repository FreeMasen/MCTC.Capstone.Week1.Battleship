from data.fields import *
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('data/battleship.db')

class DbModel(Model):
    class Meta:
        database = db

class Game(DbModel):
    complete = BoolField()
    two_player = BoolField()
    start = TimestampField()


class Player(DbModel):
    game = ForeignKeyField(Game)

class Board(DbModel):
    player = ForeignKeyField(Player)

class Grid(DbModel):
    offense = BoolField()
    board = ForeignKeyField(Board)

class Cell(DbModel):
    grid = ForeignKeyField(Grid)
    x = IntegerField()
    y = IntegerField()
    state = CellStateField()