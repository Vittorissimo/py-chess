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
        # moves = [
        #     (si + 2, sj + 1),
        #     (si + 2, sj - 1),
        #     (si - 2, sj + 1),
        #     (si - 2, sj - 1),
        #     (si + 1, sj + 2),
        #     (si + 1, sj - 2),
        #     (si - 1, sj + 2),
        #     (si - 1, sj - 2)
        # ]

        # self._feasible_set = [(x, y) for x, y in moves if 0 <= x < 8 and 0 <= y < 8]
        # copy_list = self._feasible_set

        # for i in copy_list:
        #     if(grid_matrix[i] != None):
        #         if(self._color == (grid_matrix[i].get_color())):
        #             self._feasible_set.remove(i)

        y, x = np.indices((8, 8))
        distances = np.maximum(np.abs(y - si), np.abs(x - sj))
        self._feasible_set = list(zip(*np.where(distances == 2)))

        # right
        for j in range(sj + 1, 8):
            if (grid_matrix[si, j] is None):
                self._feasible_set.append((si, j))
            else:
                if (grid_matrix[si, j].get_color() == self._set_color):
                    print(self._color)
                    print("Colore pezzo:", grid_matrix[si, j].get_color())
                    print("Sono uguali:", self._color == grid_matrix[si, j].get_color())
                    self._feasible_set.append((si, j))
                break
        
        # left
        for j in range(sj - 1, -1, -1):
            if (grid_matrix[si, j] is None):
                self._feasible_set.append((si, j))
            else:
                if (grid_matrix[si, j].get_color() == self._set_color):
                    self._feasible_set.append((si, j))
                break
        
        # under
        for i in range(si + 1, 8):
            if (grid_matrix[i, sj] is None):
                self._feasible_set.append((i, sj))
            else:
                if (grid_matrix[i, sj].get_color() == self._set_color):
                    self._feasible_set.append((i, sj))
                break
        
        # up
        for i in range(si - 1, -1, -1):
            if (grid_matrix[i, sj] is None):
                self._feasible_set.append((i, sj))
            else:
                if (grid_matrix[i, sj].get_color() == self._set_color):
                    self._feasible_set.append((i, sj))
                break
        
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