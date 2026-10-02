import numpy as np
from src.chessGame.Player import Player
from chessGame.pieces.King import King
from chessGame.pieces.Rook import Rook
from chessGame.pieces.Bishop import Bishop
from chessGame.pieces.Pawn import Pawn
from chessGame.pieces.Queen import Queen
from chessGame.pieces.Knight import Knight
from chessGame.utils.Color import Color
from chessGame.ChessBoard import ChessBoard

class GameChess:
    def __init__(self):
        self.grid = np.full((8, 8), None)
        self._player1 = Player()
        self._player2 = Player()
        self.flag = True
    
    def run(self):
        i = 0
        while(self.flag):
            if(i %2 == 0):
                for p in range(self._player1.get_pieces()):
                    qm = len(p.get_pieces())
                
                if qm == 0:
                    self.flag = False
                # white move
            else:
                for p in range(self._player2.get_pieces()):
                    qm = len(p.get_pieces())
                
                if qm == 0:
                    self.flag = False
                # black move
            
            i += 1

    def update(self):
        pass
    
    def init_grid(self):
        p1w = Pawn(Color.white, 1)
        p2w = Pawn(Color.white, 2)
        p3w = Pawn(Color.white, 3)
        p4w = Pawn(Color.white, 4)
        p5w = Pawn(Color.white, 5)
        p6w = Pawn(Color.white, 6)
        p7w = Pawn(Color.white, 7)
        p8w = Pawn(Color.white, 8)
        kn1w = Knight(Color.white, 1)
        kn2w = Knight(Color.white, 2)
        kw = King(Color.white)
        qw = Queen(Color.white)
        b1w = Bishop(Color.white, 1)
        b2w = Bishop(Color.white, 2)
        r1w = Rook(1, Color.white)
        r2w = Rook(2, Color.white)
        pieces_white = [p1w, p2w, p3w, p4w, p5w, p6w, p7w, p8w, kn1w, kn2w, kw, qw, b1w, b2w, r1w, r2w]

        p1b = Pawn(Color.black, 1)
        p2b = Pawn(Color.black, 2)
        p3b = Pawn(Color.black, 3)
        p4b = Pawn(Color.black, 4)
        p5b = Pawn(Color.black, 5)
        p6b = Pawn(Color.black, 6)
        p7b = Pawn(Color.black, 7)
        p8b = Pawn(Color.black, 8)
        kn1b = Knight(Color.black, 1)
        kn2b = Knight(Color.black, 2)
        kb = King(Color.black)
        qb = Queen(Color.black)
        b1b = Bishop(Color.black, 1)
        b2b = Bishop(Color.black, 2)
        r1b = Rook(1, Color.black)
        r2b = Rook(2, Color.black)
        pieces_black = [p1b, p2b, p3b, p4b, p5b, p6b, p7b, p8b, kn1b, kn2b, kw, qb, b1b, b2b, r1b, r2b]

        self._player1 = Player(Color.white, pieces_white)
        self._player2 = Player(Color.black, pieces_black)
        # self.grid = 
