from src.chessGame.ChessCell import ChessCell
import unittest

class ChessCellTest(unittest.TestCase):
    def test_is_free(self):
        c1 = ChessCell()
        self.assertEqual(c1.is_free(), True)
        c1.set_piece(123)
        self.assertEqual(c1.is_free(), False)