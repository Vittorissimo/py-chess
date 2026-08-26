from src.chessGame.ChessCell import ChessCell
from src.chessGame.Color import Color
import unittest

class ChessCellTest(unittest.TestCase):
    def test_is_free(self):
        c1 = ChessCell()
        self.assertEqual(c1.is_free(), True)
        c1.set_piece(123)
        self.assertEqual(c1.is_free(), False)
    
    def test_is_black(self):
        c = ChessCell()
        self.assertEqual(c.is_black(), False)
        c.set_piece(Color.black)
        self.assertEquals(c.is_black(), True)