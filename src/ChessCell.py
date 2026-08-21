class ChessCell:
    def __init__(self):
        self._chess_piece = None
    
    def is_free(self):
        if(self.cp == None):
            return True
        else:
            return False

    def is_black(self):
        if(self.cp.Color.back):
            return True
        else:
            return False

    def is_white(self):
        if(self.cp.Color.white):
            return True
        else:
            return False
    
    def set_piece(self, piece):
        pass