from chessGame.pieces.ChessPiece import ChessPiece
from chessGame.ChessBoard import ChessBoard

class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
    
    def compute_feasible_set(self, board: ChessBoard):
        self._feasible_set.clear()
        grid_matrix = board.get_raw_grid()

        si, sj = self._cell[0], self._cell[1]
        for i in range(8):
            if(((si + i) <= 7) and ((sj + i) <= 7) and (i != 0)):
                self._feasible_set.append((si + i, sj + i))
        
        for i in range(8):
            if(((si - i) >= 0) and ((sj - i) >= 0) and (i != 0)):
                self._feasible_set.append((si - i, sj - i))
        
        for i in range(8):
            if(((si + i) <= 7) and ((sj - i) >= 0) and (i != 0)):
                self._feasible_set.append((si + i, sj - i))
        
        for i in range(8):
            if(((si - i) >= 0) and ((sj + i) <= 7) and (i != 0)):
                self._feasible_set.append((si - i, sj + i))
        
        for i in range(8):
            if (i != self._cell[0]):
                self._feasible_set.append((i, sj))
        
        for i in range(8):
            if (i != self._cell[1]):
                self._feasible_set.append((si, i))
        
        for i in self._feasible_set:
            if(grid_matrix[i] != None):
                if(self._color == (grid_matrix[i].get_color())):
                    self._feasible_set.remove(i)
    
    def move(self, cell_move : tuple):
        self._cell = cell_move