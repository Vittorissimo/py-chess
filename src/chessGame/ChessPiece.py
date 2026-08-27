from src.chessGame.Status import Status

class ChessPiece:
    def __init__(self, color):
        self._set_color(color)
        self.status = Status.alive

    def get_color(self):
        return self._color
    
    def get_status(self):
        return self.status
    
    def _set_color(self, color):
        self._color = color
    
    def change_state(self):
        match self.status:
            case Status.alive:
                self.status = Status.dead
            case Status.dead:
                self.status = Status.alive