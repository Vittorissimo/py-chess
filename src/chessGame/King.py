import ChessPiece

class King(ChessPiece):
    def __init__(self):
        self.move = 1
    
    def get_move(self):
        return self.move