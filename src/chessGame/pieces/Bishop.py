import chessGame.pieces.ChessPiece as ChessPiece

class Bishop(ChessPiece):
    def __init__(self):
        self.max_move = 9
    
    def get_max_move(self):
        return self.max_move