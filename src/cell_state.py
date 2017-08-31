from enum import Enum

class CellState(Enum):
    Open = '~'
    Occupied = '■'
    Hit = '╿' 
    Missed = 'X'
    Invalid = ''