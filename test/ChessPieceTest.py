from src.chessGame.ChessPiece import ChessPiece
from src.chessGame.Color import Color
import unittest

class ChessPieceTest(unittest.TestCase):
    def test_get_color(self):
        c1 = ChessPiece(Color.white)
        self.assertEqual(c1.get_color(), Color.white)
        c2 = ChessPiece(Color.black)
        self.assertEqual(c2.get_color(), Color.black)