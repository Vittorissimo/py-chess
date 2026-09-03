from chessGame.pieces.King import King
from chessGame.utils.Color import Color
from chessGame.ChessBoard import ChessBoard
import numpy as np
import unittest

class KingTest(unittest.TestCase):
    def test_compute_fisible_set(self):
        board = ChessBoard()
        kb = King(Color.black)
        kb2 = King(Color.black)
        kw = King(Color.white)

        print(kb.get_cell())
        # todo: test

        board.set_raw_grid((5, 5), kb)
        kb.move((5,5))
        
        board.set_raw_grid((5, 6), kb2)
        kb2.move((5,6))
        
        board.set_raw_grid((5, 4), kw)
        kw.move((5,4))

        # assert su qyesto
        print(kb.get_cell())
        print(kb2.get_cell())
        print(kw.get_cell())

        kb.compute_feasible_set(board)
        kb2.compute_feasible_set(board)
        kw.compute_feasible_set(board)
        print("king black: ", kb.get_feasible_set())
        print("king black2: ", kb2.get_feasible_set())
        print("king white: ", kw.get_feasible_set())

        

if __name__ == "__main__":
    unittest.main()