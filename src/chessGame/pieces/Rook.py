from chessGame.pieces.ChessPiece import ChessPiece
from chessGame.ChessBoard import ChessBoard
from chessGame.utils.Color import Color

class Rook(ChessPiece):
    def __init__(self, number_position, color):
        super().__init__(color)
        self.set_cell(number_position)
    
    def set_cell(self, value):
        if(value == 1):
            if (self._color == Color.white):
                self._cell = (7, 0)
            else:
                self._cell = (0, 7)
        else:
            if(self._color == Color.white):
                self._cell = (7, 7)
            else:
                self._cell = (0, 0)
    
    def move(self, cell_move : tuple):
        self._cell = cell_move
    
    def compute_feasible_set(self, board: ChessBoard):
        self._feasible_set.clear()
        grid_matrix = board.get_raw_grid()

        si, sj = self._cell[0], self._cell[1]
        for i in range(8):
            if (i != self._cell[0]):
                self.feasible_set.append(i, sj)
        
        for i in range(8):
            if (i != self._cell[1]):
                self.feasible_set.append(si, i)