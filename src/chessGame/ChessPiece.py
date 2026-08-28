from src.chessGame.Status import Status
from src.chessGame.Color import Color

class ChessPiece:
    def __init__(self, color):
        self._set_color(color)
        self.status = Status.alive

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
        if(self.status == Status.alive):
            return True
        else:
            return False
    
    def is_dead(self):
        if(self.status == Status.dead):
            return True
        else:
            return False
    
    def _set_color(self, color):
        self._color = color
    
    def change_state(self):
        match self.status:
            case Status.alive:
                self.status = Status.dead
            case Status.dead:
                self.status = Status.alive