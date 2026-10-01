from chessGame.pieces.ChessPiece import ChessPiece
from chessGame.utils.Color import Color

class Player:
    def __init__(self, color):
        self.pieces = []
        self.color = color

    def get_pieces(self):
        return self.pieces
    
    def get_color(self):
        return self.color