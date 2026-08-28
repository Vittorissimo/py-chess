import chessGame.pieces.ChessPiece as ChessPiece

class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.first_move = True
    
    def get_first_move(self):
        return self.first_move