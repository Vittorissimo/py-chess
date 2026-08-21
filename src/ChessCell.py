class EmptyCell:
    def __init__(self, chess_piece):
        self.cp = chess_piece
    
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