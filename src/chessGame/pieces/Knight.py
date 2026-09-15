from chessGame.pieces.ChessPiece import ChessPiece
from chessGame.ChessBoard import ChessBoard
from chessGame.utils.Color import Color
import numpy as np

class Knight(ChessPiece):
    def __init__(self, color, value):
        super().__init__(color)
        self.set_cell(value)
    
    def move(self, cell_move : tuple):
        self._cell = cell_move
    
    def set_cell(self, value):
        if(value == 1):
            if (self._color == Color.white):
                self._cell = (7, 1)
            else:
                self._cell = (0, 6)
        else:
            if(self._color == Color.white):
                self._cell = (7, 6)
            else:
                self._cell = (0, 1)
        
    def compute_feasible_set(self, board: ChessBoard):
        self._feasible_set.clear()
        grid_matrix     = board.get_raw_grid()

        si, sj = self._cell[0], self._cell[1]
        moves = [
            (si + 2, sj + 1),
            (si + 2, sj - 1),
            (si - 2, sj + 1),
            (si - 2, sj - 1),
            (si + 1, sj + 2),
            (si + 1, sj - 2),
            (si - 1, sj + 2),
            (si - 1, sj - 2)
        ]

        self._feasible_set = [(x, y) for x, y in moves if 0 <= x < 8 and 0 <= y < 8]
