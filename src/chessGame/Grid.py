import Letter
import numpy as np
import ChessCell

class Grid:
    def __init__(self):
        self._row_column = 8
        self._grid = np.empty((self._row_column, self._row_column), dtype=ChessCell)

        for row in range(self._row_column):
            for column in range(self._row_column):
                self._grid[row, column] = ChessCell()
    
    def get_cell(self, row, column):
        return self._grid[row, column]
    
    def insert_piece(self, row, column, piece):
        self._grid[row, column].set_piece(piece)