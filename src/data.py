import sqlite3

Class Data():
    def __init__(self):        
        self.conn = sqlite3.connect('battleship.db')

    def get_game(self):
        pass
    
    def save_game(self):
        pass
        