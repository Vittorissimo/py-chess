import Status

class ChessPiece:
    def __init__(self, color):
        self.color = color
        self.status = Status.alive

    def get_color(self):
        return self.color
    
    def get_status(self):
        return self.status