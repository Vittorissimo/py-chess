import numpy as np
from src.chessGame.Player import Player

class GameChess:
    def __init__(self):
        self.grid = np.full((8, 8), None)
        self._player1 = Player()
        self._player2 = Player()
    
    def run(self):
        pass

    def update(self):
        pass
    
    def init_grid(self):
        pass