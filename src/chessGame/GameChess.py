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
                for p in range(self._player1.get_pieces()):
                    qm = len(p.get_pieces())
                
                if qm == 0:
                    self.flag = False
                # white move
            else:
                for p in range(self._player2.get_pieces()):
                    qm = len(p.get_pieces())
                
                if qm == 0:
                    self.flag = False
                # black move
            
            i += 1

    def update(self):
        pass
    
    def init_grid(self):
        pass