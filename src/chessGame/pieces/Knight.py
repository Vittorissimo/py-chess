import chessGame.pieces.ChessPiece as ChessPiece

class Knight(ChessPiece):
    def __init__(self):
        self.move_a = 1
        self.move_b = 2
    
    def get_move(self):
        return self.move_a, self.move_b