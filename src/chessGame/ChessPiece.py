from src.chessGame.Status import Status
from src.chessGame.Color import Color

class ChessPiece:
    def __init__(self, color):
        self._set_color(color)
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
    
    def _set_state(self):
        self._status = Status.alive
    
    def kill(self):
        self._status = Status.dead