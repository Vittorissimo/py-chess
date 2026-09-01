import numpy as np

class ChessBoard:
    def __init__(self):
        self._matrix = np.empty((8, 8), dtype=object)
        self._matrix.fill(None)
        self.letter_dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    
    def get_cell(self, column, row):
        if((row <= 8) or (row >= 1)):
            return self._matrix[8 - row, self.letter_dictionary[column]]
        #

    def set_cell(self, column, row, piece):
        if((row <= 8) or (row >= 1)):
            self._matrix[8 - row, self.letter_dictionary[column]] = piece