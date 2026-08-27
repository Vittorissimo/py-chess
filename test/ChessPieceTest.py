from src.chessGame.ChessPiece import ChessPiece
from src.chessGame.Color import Color
from src.chessGame.Status import Status
import unittest

class ChessPieceTest(unittest.TestCase):
    def test_get_color(self):
        c1 = ChessPiece(Color.white)
        self.assertEqual(c1.get_color(), Color.white)
        c2 = ChessPiece(Color.black)
        self.assertEqual(c2.get_color(), Color.black)
    
    def test_get_status(self):
        c1 = ChessPiece(Color.white)
        self.assertEqual(c1.get_status(), Status.alive)
        c1.change_state()
        self.assertEqual(c1.get_status(), Status.dead)
    
    def test_change_state(self):
        c1 = ChessPiece(Color.white)
        self.assertEqual(c1.get_status(), Status.alive)
        c1.change_state()
        self.assertEqual(c1.get_status(), Status.dead)
        c1.change_state()
        self.assertEqual(c1.get_status(), Status.alive)