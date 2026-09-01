from chessGame.pieces.King import King
from chessGame.utils.Color import Color
import numpy as np
import unittest

class KingTest(unittest.TestCase):
    def test_compute_fisible_set(self):
        self.grid = np.full((8, 8), None)

        k = King(Color.black)
        k.compute_fisible_set(self.grid)
        self.assertEqual(sorted(k.get_fisible_set()), sorted([[1, 6], [2, 6], [2, 5], [2, 4], [1, 4], [0, 4], [0, 5], [0, 6]]))
        

if __name__ == "__main__":
    unittest.main()