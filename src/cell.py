from src.cell_state import CellState

class Cell():
    def __init__(self):
        self.state = CellState.Open
    
    
    def display(self):
        return self.state.value