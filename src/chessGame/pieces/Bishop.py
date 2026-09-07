from chessGame.pieces.ChessPiece import ChessPiece
from chessGame.ChessBoard import ChessBoard
from chessGame.utils.Color import Color

class Bishop(ChessPiece):
    def __init__(self, color, number):
        super().__init__(color)
        self.set_cell(number)
    
    def set_cell(self, value):
        if(value == 1):
            if (self._color == Color.white):
                self._cell = (7, 2)
            else:
                self._cell = (0, 2)
        else:
            if(self._color == Color.white):
                self._cell = (7, 5)
            else:
                self._cell = (0, 5)
    
    def move(self, cell_move : tuple):
        self._cell = cell_move
    
    def compute_feasible_set(self, board: ChessBoard):
        self._feasible_set.clear()
        grid_matrix = board.get_raw_grid()

        si, sj = self._cell[0], self._cell[1]
        for i in range(8):
            if (i != si and i != sj):
                self._feasible_set.append((si + i, sj + i))
        
        for i in range(8):
            if (i != si and i != sj):
                self._feasible_set.append((si - i, sj - i))
        
        for i in range(8):
            if (i != si and i != sj):
                self._feasible_set.append((si + i, sj - i))
        
        for i in range(8):
            # if()
            if (i != si and i != sj):
                self._feasible_set.append((si - i, sj + i))
        
        for i in self._feasible_set:
            if(grid_matrix[i] != None):
                if(self._color == (grid_matrix[i].get_color())):
                    self._feasible_set.remove(i)