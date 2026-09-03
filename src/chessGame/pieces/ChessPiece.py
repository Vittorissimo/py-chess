from chessGame.utils.Status import Status
from chessGame.utils.Color import Color

class ChessPiece:
    def __init__(self, color):
        self._set_color(color)
        self._feasible_set = []
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
    
    def get_color(self):
        return self._color
    
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
    
    def compute_feasible_set(self, board):
        pass

    def get_feasible_set(self):        
        return self._feasible_set
    
    def get_cell(self):
        return self._cell