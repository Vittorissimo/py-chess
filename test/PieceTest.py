from chessGame.pieces.King import King
from chessGame.pieces.Rook import Rook
from chessGame.pieces.Bishop import Bishop
from chessGame.pieces.Pawn import Pawn
from chessGame.pieces.Queen import Queen
from chessGame.pieces.Knight import Knight
from chessGame.utils.Color import Color
from chessGame.ChessBoard import ChessBoard
import numpy as np
import unittest

class PieceTest(unittest.TestCase):
    def test_compute_fisible_set(self):
        board = ChessBoard()

        # King
        # kb = King(Color.black)
        # kb2 = King(Color.black)
        # kw = King(Color.white)

        # print(kb.get_cell())
        # # todo: test

        # board.set_raw_grid((5, 5), kb)
        # kb.move((5,5))
        
        # board.set_raw_grid((5, 6), kb2)
        # kb2.move((5,6))
        
        # board.set_raw_grid((5, 4), kw)
        # kw.move((5,4))

        # assert su qyesto
        # print(kb.get_cell())
        # print(kb2.get_cell())
        # print(kw.get_cell())

        # kb.compute_feasible_set(board)
        # kb2.compute_feasible_set(board)
        # kw.compute_feasible_set(board)
        # print("king black: ", kb.get_feasible_set())
        # print("king black2: ", kb2.get_feasible_set())
        # print("king white: ", kw.get_feasible_set())

        # Rook
        # r = Rook(1, Color.white)
        # r.move((3, 4))
        # r.compute_feasible_set(board)
        # print(r.get_feasible_set())

        # Bishop
        # b = Bishop(Color.white, 1)
        # b.move((3, 3))
        # b.compute_feasible_set(board)
        # print(b.get_feasible_set())

        # todo
        # Pawn
        # pw = Pawn(Color.white)
        # pb = Pawn(Color.black)
        # pw.move((5, 5))
        # pb.move((6, 5))
        # board.set_raw_grid((5, 5), pw)
        # board.set_raw_grid((5, 6), pb)
        # pw.compute_feasible_set(board)
        # # pb.compute_feasible_set(board)
        # print("p-white: ", pw.get_feasible_set())
        # # print("p-black: ", pb.get_feasible_set())


        #Queen
        # q = Queen(Color.white)
        # q.move((3, 3))
        # q.compute_feasible_set(board)
        # print(q.get_feasible_set())

        # Knight
        k = Knight(Color.white, 1)
        k.move((3, 3))
        board.set_raw_grid((3, 3), k)
        b = Bishop(Color.white, 1)
        b.move((5, 4))
        board.set_raw_grid((5, 4), b)
        k.compute_feasible_set(board)
        print(k.get_feasible_set())
        b2 = Bishop(Color.white, 1)
        b2.move((2, 1))
        board.set_raw_grid((2, 1), b2)
        k.compute_feasible_set(board)
        print(k.get_feasible_set())

        

if __name__ == "__main__":
    unittest.main()