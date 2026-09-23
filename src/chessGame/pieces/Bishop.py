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
        # Right + Under
        for i in range(1, 8):
            x = si + i
            y = sj + i

            if (x >= 8 or y >= 8):
                break

            if (grid_matrix[x, y] is None):
                self._feasible_set.append((x, y))
            else:
                if (grid_matrix[x, y].get_color() != self._color):
                    self._feasible_set.append((x, y))
                break

        # Left + Under
        for i in range(1, 8):
            x = si + i
            y = sj - i

            if (x >= 8 or y < 0):
                break

            if (grid_matrix[x, y] is None):
                self._feasible_set.append((x, y))
            else:
                if (grid_matrix[x, y].get_color() != self._color):
                    self._feasible_set.append((x, y))
                break

        # Right + Up
        for i in range(1, 8):
            x = si - i
            y = sj + i

            if (x < 0 or y >= 8):
                break

            if (grid_matrix[x, y] is None):
                self._feasible_set.append((x, y))
            else:
                if (grid_matrix[x, y].get_color() != self._color):
                    self._feasible_set.append((x, y))
                break

        # Left + Up
        for i in range(1, 8):
            x = si - i
            y = sj - i

            if (x < 0 or y < 0):
                break

            if (grid_matrix[x, y] is None):
                self._feasible_set.append((x, y))
            else:
                if (grid_matrix[x, y].get_color() != self._color):
                    self._feasible_set.append((x, y))
                break