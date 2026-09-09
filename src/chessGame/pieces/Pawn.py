from chessGame.pieces.ChessPiece import ChessPiece
from chessGame.ChessBoard import ChessBoard

class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.first_move = True
    
    def move(self, cell_move : tuple):
        self._cell = cell_move
        self.first_move = False

    def compute_feasible_set(self, board: ChessBoard):
        self._feasible_set.clear()
        grid_matrix     = board.get_raw_grid()

        si, sj = self._cell[0], self._cell[1]
        if(self.first_move):
            for i in range(2):
                self._feasible_set.append((si + i, sj))
                
        else:
            self._feasible_set.append((si + 1), sj)

        for i in self._feasible_set:
            if(grid_matrix[i] != None):
                if(self._color == (grid_matrix[i].get_color())):
                    self._feasible_set.remove(i)