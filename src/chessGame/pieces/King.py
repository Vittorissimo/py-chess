from chessGame.pieces.ChessPiece import ChessPiece
from chessGame.ChessBoard import ChessBoard
from chessGame.utils.Color import Color

class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.set_cell()
    
    def compute_feasible_set(self, board: ChessBoard):
        self._feasible_set.clear()
        grid_matrix     = board.get_raw_grid()

        # cicla i e j per riga e colonna
        # nella matrice grezza (grid_matrix)
        si, sj = self._cell[0], self._cell[1]
        for i in range(3):
            for j in range(3):
                if((i,j) != (1,1)):
                    i_d, j_d = si + i - 1, sj + j - 1
                    if ((i_d >= 0 and j_d >= 0) and (i_d <= 7 and j_d <= 7)):
                        self._feasible_set.append((i_d, j_d))

        # nemici e amici
        for i in self._feasible_set:
            if(grid_matrix[i] != None):
                if(self._color == (grid_matrix[i].get_color())):
                    self._feasible_set.remove(i)
    
    def set_cell(self):
        if (self._color == Color.white):
            self._cell = (7, 4)
        else:
            self._cell = (0, 4)

    def move(self, cell_move : tuple):
        self._cell = cell_move

    
    def value_modificator(self, value_letter, board):
        key = next(key for key, value in board.letter_dictionary.items() if value == value_letter)
        print(key)
        return key