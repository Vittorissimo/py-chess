import numpy as np
from src.chessGame.Player import Player

class GameChess:
    def __init__(self):
        self.grid = np.full((8, 8), None)
        self._player1 = Player()
        self._player2 = Player()
        self.flag = True
    
    def run(self):
        i = 0
        while(self.flag):
            if(i %2 == 0):
                self._player1
                # white move
            else:
                self._player2
                # black move
            
            i += 1

    def update(self):
        pass
    
    def init_grid(self):
        pass