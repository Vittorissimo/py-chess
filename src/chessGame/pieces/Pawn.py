from chessGame.pieces.ChessPiece import ChessPiece
from chessGame.ChessBoard import ChessBoard
from chessGame.utils.Color import Color

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
        print("PAWN POSITION:", self._cell)
        print("FORWARD:", grid_matrix[si + 1, sj])
        print("Is None?", grid_matrix[si + 1, sj] is None)
        if(self.first_move):
            if (self._color == Color.white):
                for i in range(3):
                    if (i != 0 and grid_matrix[si - i, sj] is None):
                        self._feasible_set.append((si - i, sj))
                        print("p-white: ", self.get_feasible_set())
            
            if (self._color == Color.black):
                for i in range(3):
                    if (i != 0 and grid_matrix[si + i, sj] is None):
                        self._feasible_set.append((si + i, sj))
                        print("p-black: ", self.get_feasible_set())
                
        else:
            if (self._color == Color.white):
                if (grid_matrix[si - 1, sj] is None):
                    print(grid_matrix)
                    self._feasible_set.append((si - 1, sj))
                    print("p-white: ", self.get_feasible_set())
            else:
                if (grid_matrix[si + 1, sj] is None):
                    print(grid_matrix)
                    self._feasible_set.append((si + 1, sj))
                    print("p-black: ", self.get_feasible_set())
        
        if(self._color == Color.white):
            if (grid_matrix[si - 1, sj - 1] != None) and (self._color != grid_matrix[si - 1, sj - 1]):
                self._feasible_set.append((si - 1, sj - 1))
            if (grid_matrix[si - 1, sj + 1] != None) and (self._color != grid_matrix[si - 1, sj + 1]):
                self._feasible_set.append((si - 1, sj + 1))
        
        else:
            if (grid_matrix[si + 1, sj + 1] != None) and (self._color != grid_matrix[si + 1, sj + 1]):
                self._feasible_set.append((si + 1, sj + 1))
            if (grid_matrix[si + 1, sj - 1] != None) and (self._color != grid_matrix[si + 1, sj - 1]):
                self._feasible_set.append((si + 1, sj - 1))

        print("p-white: ", self.get_feasible_set())

        for i in self._feasible_set:
            if(grid_matrix[i] != None):
                if(self._color == (grid_matrix[i].get_color())):
                    self._feasible_set.remove(i)
    