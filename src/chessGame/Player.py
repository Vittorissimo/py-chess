from chessGame.pieces.ChessPiece import ChessPiece
from chessGame.utils.Color import Color

class Player:
    def __init__(self, color, pieces_color: list):
        self.pieces = pieces_color
        self.color = color

    def get_pieces(self):
        return self.pieces
    
    def get_color(self):
        return self.color
    
    def add_piece(self, piece):
        self.pieces.append(piece)
    
    def remove_piece(self, piece):
        self.pieces.remove(piece)
    
    