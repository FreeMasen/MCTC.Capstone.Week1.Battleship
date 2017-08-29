from src.cell_state import CellState
from peewee import Field
class CellStateField(Field):
    db_field = 'cell_state'

    def db_value(self, value):
        if value == 0:
            return CellState.Open
        if value == 1:
            return CellState.Occupied
        if value == 2:
            return CellState.Hit
        if value == 3:
            return CellState.Missed
        return CellState.Invalid

    def python_value(self, value):
        if value == CellState.Open:
            return 0
        if value == CellState.Occupied:
            return 1
        if value == CellState.Hit:
            return 2
        if value == CellState.Missed:
            return 3
        if value == CellState.Invalid:
            return -1
        
class BoolField(Field):
    db_field = 'bool'

    def db_value(self, value):
        if (value == 1):
            return True
        return False

    def python_value(self, value):
        if (value == True): return 1
        return 0