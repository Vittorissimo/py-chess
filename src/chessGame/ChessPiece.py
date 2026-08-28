from src.chessGame.Status import Status
from src.chessGame.Color import Color

class ChessPiece:
    def __init__(self, color):
        self._set_color(color)
        self._fisible_set = {}
        self._cell = ()
        self._status = Status.alive

    def is_white(self):
        if(self._color == Color.white):
            return True
        else:
            return False
    
    def is_black(self):
        if(self._color == Color.black):
            return True
        else:
            return False
    
    def is_alive(self):
        if(self._status == Status.alive):
            return True
        else:
            return False
    
    def is_dead(self):
        if(self._status == Status.dead):
            return True
        else:
            return False
    
    def _set_color(self, color):
        self._color = color
    
    def kill(self):
        self._status = Status.dead
    
    def compute_fisible_set(self, grid):
        pass

    def get_fisible_set(self):        
        return self._fisible_set