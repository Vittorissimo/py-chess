class ChessCell:
    def __init__(self):
        self._chess_piece = None
    
    def is_free(self):
        if(self._chess_piece == None):
            return True
        else:
            return False

    def is_black(self):
        if(self._chess_piece.Color.back):
            return True
        else:
            return False

    def is_white(self):
        if(self._chess_piece.Color.white):
            return True
        else:
            return False
    
    def set_piece(self, piece):
        self._chess_piece = piece