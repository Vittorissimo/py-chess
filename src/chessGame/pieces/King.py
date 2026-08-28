import chessGame.pieces.ChessPiece as ChessPiece

class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.move = 1
    
    def get_move(self):
        return self.move
    
    def compute_fisible_set(self):
        self.