import numpy as np
from chessGame.pieces.ChessPiece import ChessPiece

class ChessBoard:
    def __init__(self):
        self._matrix = np.empty((8, 8), dtype=object)
        self._matrix.fill(None)
        self.letter_dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    
    def get_cell(self, column, row):
        if((row <= 8) or (row >= 1)):
            return self._matrix[8 - row, self.letter_dictionary[column]]
        #

    def set_cell(self, column, row, piece):
        if((row <= 8) or (row >= 1)):
            self._matrix[8 - row, self.letter_dictionary[column]] = piece

    def get_raw_grid(self):
        return self._matrix
    
    def set_raw_grid(self, pos: tuple, piece: ChessPiece):
        if(((pos[0] <= 7) and (pos[0] >= 0) and (pos[1] <= 7) and (pos[1] >= 0))):
            self._matrix[pos] = piece