import ChessPiece

class Pawn(ChessPiece):
    def __init__(self):
        self.max_move = 2
    
    def get_max_move(self):
        return self.max_move